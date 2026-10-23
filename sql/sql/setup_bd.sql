CREATE DATABASE IF NOT EXISTS bd_noticias CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'usuario_noticias'@'localhost' IDENTIFIED BY 'NoticiasPass2026!';

GRANT ALL PRIVILEGES ON bd_noticias.* TO 'usuario_noticias'@'localhost';

FLUSH PRIVILEGES;