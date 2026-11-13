CREATE DATABASE IF NOT EXISTS app_movil_db;

USE app_movil_db;

CREATE TABLE IF NOT EXISTS perfiles_moviles (
    id_perfil INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    gemas INT NOT NULL DEFAULT 50,
    racha_dias INT NOT NULL DEFAULT 1,
    notificaciones_activas BOOLEAN NOT NULL DEFAULT TRUE,
    meses_suscripcion INT NOT NULL DEFAULT 0,
    es_pro BOOLEAN NOT NULL DEFAULT FALSE,
    tipo VARCHAR(10) NOT NULL DEFAULT 'Movil'
);

INSERT INTO perfiles_moviles
    (username, gemas, racha_dias, notificaciones_activas, meses_suscripcion, es_pro, tipo)
VALUES
    ('leonel', 50, 1, TRUE, 0, FALSE, 'Movil'),
    ('leonel_pro', 80, 5, TRUE, 3, TRUE, 'Pro')
ON DUPLICATE KEY UPDATE username = username;
