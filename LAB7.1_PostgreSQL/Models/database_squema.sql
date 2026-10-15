CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    passw VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO users (username, passw, nombre) VALUES ('admin', 'admin123', 'Super admin');

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);