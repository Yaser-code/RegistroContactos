CREATE DATABASE contactosPython;
USE contactosPython;

-- Crear tablas
CREATE TABLE contacto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL,
    telefono INTEGER(9) NOT NULL,
    pais VARCHAR(20) NOT NULL
);