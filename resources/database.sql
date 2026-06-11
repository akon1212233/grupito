-- drop database adopcionMascotas;
-- MySQL Script estructurado estilo MySQL Workbench
-- Model: Adopción de Mascotas v1.0

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema adopcionMascotas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `adopcionMascotas` DEFAULT CHARACTER SET utf8 ;
USE `adopcionMascotas` ;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`tipos_razas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`tipos_razas` (
  `id_tipo_raza` INT NOT NULL AUTO_INCREMENT,
  `nombre_tipo_raza` VARCHAR(100) NOT NULL,
  `descripcion_raza` VARCHAR(200) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0, -- Borrado lógico (0: Activo, 1: Oculto/Eliminado)
  PRIMARY KEY (`id_tipo_raza`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`razas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`razas` (
  `id_raza` INT NOT NULL AUTO_INCREMENT,
  `nombre_raza` VARCHAR(100) NOT NULL,
  `id_tipo_raza` INT NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_raza`),
  INDEX `fk_razas_tipos_razas_idx` (`id_tipo_raza` ASC) VISIBLE,
  CONSTRAINT `fk_razas_tipos_razas`
    FOREIGN KEY (`id_tipo_raza`)
    REFERENCES `adopcionMascotas`.`tipos_razas` (`id_tipo_raza`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`sexos_mascotas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`sexos_mascotas` (
  `id_sexo_mascota` INT NOT NULL AUTO_INCREMENT,
  `tipo_sexo_mascota` VARCHAR(10) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_sexo_mascota`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`mascotas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`mascotas` (
  `id_mascota` INT NOT NULL AUTO_INCREMENT,
  `nombre_mascota` VARCHAR(100) NULL,
  `edad` INT NULL,
  `id_raza` INT NOT NULL,
  `id_sexo_mascota` INT NOT NULL,
  `id_usuario` INT NULL,
  `fecha_nacimiento` date not null,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_mascota`),
  INDEX `fk_mascotas_razas1_idx` (`id_raza` ASC) VISIBLE,
  INDEX `fk_mascotas_sexos_mascotas1_idx` (`id_sexo_mascota` ASC) VISIBLE,
  CONSTRAINT `fk_mascotas_razas1`
    FOREIGN KEY (`id_raza`)
    REFERENCES `adopcionMascotas`.`razas` (`id_raza`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mascotas_sexos_mascotas1`
    FOREIGN KEY (`id_sexo_mascota`)
    REFERENCES `adopcionMascotas`.`sexos_mascotas` (`id_sexo_mascota`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`regiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`regiones` (
  `id_region` INT NOT NULL AUTO_INCREMENT,
  `nombre_region` VARCHAR(100) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_region`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`comunas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`comunas` (
  `id_comuna` INT NOT NULL AUTO_INCREMENT,
  `nombre_comuna` VARCHAR(100) NOT NULL,
  `id_region` INT NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_comuna`),
  INDEX `fk_comunas_regiones1_idx` (`id_region` ASC) VISIBLE,
  CONSTRAINT `fk_comunas_regiones1`
    FOREIGN KEY (`id_region`)
    REFERENCES `adopcionMascotas`.`regiones` (`id_region`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`direcciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`direcciones` (
  `id_direccion` INT NOT NULL AUTO_INCREMENT,
  `calle` VARCHAR(100) NOT NULL,
  `numero` VARCHAR(10) NULL,
  `departamento` VARCHAR(10) NULL,
  `id_comuna` INT NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_direccion`),
  INDEX `fk_direcciones_comunas1_idx` (`id_comuna` ASC) VISIBLE,
  CONSTRAINT `fk_direcciones_comunas1`
    FOREIGN KEY (`id_comuna`)
    REFERENCES `adopcionMascotas`.`comunas` (`id_comuna`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`personas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`personas` (
  `id_persona` INT NOT NULL AUTO_INCREMENT,
  `RUT` VARCHAR(20) NULL,
  `nombre` VARCHAR(50) NOT NULL,
  `apellido` VARCHAR(50) NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_persona`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`empleados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`empleados` (
  `id_empleado` INT NOT NULL AUTO_INCREMENT,
  `id_persona` INT NOT NULL,
  `id_direccion` INT NOT NULL,
  `cargo` VARCHAR(100) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_empleado`),
  INDEX `fk_empleados_personas1_idx` (`id_persona` ASC) VISIBLE,
  INDEX `fk_empleados_direcciones1_idx` (`id_direccion` ASC) VISIBLE,
  CONSTRAINT `fk_empleados_personas1`
    FOREIGN KEY (`id_persona`)
    REFERENCES `adopcionMascotas`.`personas` (`id_persona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_empleados_direcciones1`
    FOREIGN KEY (`id_direccion`)
    REFERENCES `adopcionMascotas`.`direcciones` (`id_direccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`adoptantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`adoptantes` (
  `id_adoptante` INT NOT NULL AUTO_INCREMENT,
  `id_persona` INT NOT NULL,
  `id_direccion` INT NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_adoptante`),
  INDEX `fk_adoptantes_personas1_idx` (`id_persona` ASC) VISIBLE,
  INDEX `fk_adoptantes_direcciones1_idx` (`id_direccion` ASC) VISIBLE,
  CONSTRAINT `fk_adoptantes_personas1`
    FOREIGN KEY (`id_persona`)
    REFERENCES `adopcionMascotas`.`personas` (`id_persona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_adoptantes_direcciones1`
    FOREIGN KEY (`id_direccion`)
    REFERENCES `adopcionMascotas`.`direcciones` (`id_direccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`tipos_usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`tipos_usuarios` (
  `id_tipo_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre_tipo` VARCHAR(50) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_tipo_usuario`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`usuarios` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NULL,
  `password_hash` VARCHAR(255) NULL, 
  `email` VARCHAR(100) NOT NULL,
  `id_persona` INT NOT NULL,
  `id_tipo_usuario` INT NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  INDEX `fk_usuarios_personas1_idx` (`id_persona` ASC) VISIBLE,
  INDEX `fk_usuarios_tipos_usuarios1_idx` (`id_tipo_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_personas1`
    FOREIGN KEY (`id_persona`)
    REFERENCES `adopcionMascotas`.`personas` (`id_persona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_tipos_usuarios1`
    FOREIGN KEY (`id_tipo_usuario`)
    REFERENCES `adopcionMascotas`.`tipos_usuarios` (`id_tipo_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`tipos_estados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`tipos_estados` (
  `id_tipo_estado` INT NOT NULL AUTO_INCREMENT,
  `nombre_tipo` VARCHAR(100) NOT NULL,
  `descripcion_tipo` VARCHAR(200) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_tipo_estado`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`estados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`estados` (
  `id_estado` INT NOT NULL AUTO_INCREMENT,
  `nombre_estado` VARCHAR(100) NOT NULL,
  `id_tipo_estado` INT NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_estado`),
  INDEX `fk_estados_tipos_estados1_idx` (`id_tipo_estado` ASC) VISIBLE,
  CONSTRAINT `fk_estados_tipos_estados1`
    FOREIGN KEY (`id_tipo_estado`)
    REFERENCES `adopcionMascotas`.`tipos_estados` (`id_tipo_estado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `adopcionMascotas`.`solicitudes_adopciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `adopcionMascotas`.`solicitudes_adopciones` (
  `id_solicitud_adopcion` INT NOT NULL AUTO_INCREMENT,
  `id_mascota` INT NOT NULL,
  `id_adoptante` INT NOT NULL,
  `id_empleado` INT NOT NULL,
  `id_estado` INT NOT NULL,
  `fecha_solicitud` DATE NULL,
  `observaciones` varchar(200) not null,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` INT NULL,
  `deleted` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id_solicitud_adopcion`),
  INDEX `fk_solicitudes_adopciones_mascotas1_idx` (`id_mascota` ASC) VISIBLE,
  INDEX `fk_solicitudes_adopciones_adoptantes1_idx` (`id_adoptante` ASC) VISIBLE,
  INDEX `fk_solicitudes_adopciones_empleados1_idx` (`id_empleado` ASC) VISIBLE,
  INDEX `fk_solicitudes_adopciones_estados1_idx` (`id_estado` ASC) VISIBLE,
  CONSTRAINT `fk_solicitudes_adopciones_mascotas1`
    FOREIGN KEY (`id_mascota`)
    REFERENCES `adopcionMascotas`.`mascotas` (`id_mascota`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_solicitudes_adopciones_adoptantes1`
    FOREIGN KEY (`id_adoptante`)
    REFERENCES `adopcionMascotas`.`adoptantes` (`id_adoptante`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_solicitudes_adopciones_empleados1`
    FOREIGN KEY (`id_empleado`)
    REFERENCES `adopcionMascotas`.`empleados` (`id_empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_solicitudes_adopciones_estados1`
    FOREIGN KEY (`id_estado`)
    REFERENCES `adopcionMascotas`.`estados` (`id_estado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `adopcionMascotas` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `adopcionMascotas`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- =====================================================
-- INSERCIÓN DE DATOS DE PRUEBA 
-- =====================================================
USE `adopcionMascotas`;

INSERT INTO tipos_razas (nombre_tipo_raza, descripcion_raza) VALUES
('Perro', 'Animal doméstico canino'),
('Gato', 'Animal doméstico felino'),
('Conejo', 'Animal doméstico roedor');

INSERT INTO razas (nombre_raza, id_tipo_raza) VALUES
('Bull Terrier', 1),
('Bull Dog Francés', 1),
('Labrador', 1),
('Siamés', 2),
('Angora', 2);

INSERT INTO sexos_mascotas (tipo_sexo_mascota) VALUES
('Macho'),
('Hembra');

INSERT INTO mascotas (nombre_mascota, id_raza, id_sexo_mascota, fecha_nacimiento) VALUES
('Cholito', 1, 1, '2020-05-10'),
('Luna', 2, 2, '2021-08-15'),
('Kira', 3, 2, '2019-02-20');

INSERT INTO regiones (nombre_region) VALUES
('Región de Coquimbo'),
('Región de Valparaíso'),
('Región Metropolitana'),
('Región del Maule');

INSERT INTO comunas (nombre_comuna, id_region) VALUES
('La Serena', 1),
('Viña del Mar', 2),
('Santiago', 3),
('Talca', 4);

INSERT INTO direcciones (calle, numero, departamento, id_comuna) VALUES
('Av. del Mar', '1234', NULL, 1),
('Calle Valparaíso', '567', 'Depto 3', 2),
('Av. Providencia', '890', NULL, 3),
('Calle 1 Sur', '321', 'Depto 5', 4);

INSERT INTO personas (RUT, nombre, apellido, telefono, fecha_nacimiento) VALUES
('20245645-4', 'Daniel', 'Carranza', '+56 9 5678 2345', '2000-04-08'),
('22245645-4', 'Benjamin', 'Cortinez', '+56 9 5674 2335', '2001-06-06'),
('21245645-4', 'Akon', 'Bustamante', '+56 9 5678 2355', '2004-05-02'),
('19245645-4', 'Martin', 'Correa', '+56 9 4678 2345', '2000-08-05');

INSERT INTO empleados (id_persona, id_direccion, cargo) VALUES
(1, 2, 'Veterinario Jefe'),
(2, 1, 'Administrativo de Adopciones');

INSERT INTO adoptantes (id_persona, id_direccion) VALUES
(3, 3),
(4, 4);

INSERT INTO tipos_usuarios (nombre_tipo) VALUES
('Administrador'),
('Empleado'),
('Adoptante');

-- MEJORA PARA PRUEBAS: Contraseñas en texto plano (ej: '123456')
INSERT INTO usuarios (username, password_hash, email, id_persona, id_tipo_usuario) VALUES
('daniel.carranza', 'daniel.carranza@email.com','123456', 1, 1),
('benjamin.cortinez', 'benjamin.cortinez@email.com', '123456', 2, 2),
('akon.bustamante', 'akon.bustamante@email.com', '123456', 3, 3),
('martin.correa', 'martin.correa@email.com', '123456', 4, 3);

INSERT INTO tipos_estados (nombre_tipo, descripcion_tipo) VALUES
('Solicitud', 'Estados relacionados al proceso de solicitud de adopción'),
('Mascota', 'Estados relacionados a la disponibilidad de la mascota');

INSERT INTO estados (nombre_estado, id_tipo_estado) VALUES
('Pendiente', 1),
('En Revisión', 1),
('Aprobada', 1),
('Rechazada', 1),
('Disponible', 2),
('Adoptada', 2),
('En Tratamiento', 2);

INSERT INTO solicitudes_adopciones (id_mascota, id_adoptante, id_empleado, id_estado, fecha_solicitud, observaciones) VALUES
(1, 1, 3, 1, '2024-01-15', 'Solicitud recién creada, pendiente de asignación a un empleado.'),
(2, 2, 2, 3, '2024-02-20', 'Solicitud aprobada. Se coordinó visita domiciliaria.'),
(3, 1, 1, 4, '2024-03-10', 'Rechazada: El adoptante no cuenta con el espacio mínimo requerido para la raza.');