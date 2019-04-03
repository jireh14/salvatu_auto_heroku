CREATE DATABASE salva;

USE salva;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE usuario(
    email varchar(35) NOT NULL PRIMARY KEY);


CREATE TABLE coche( 
    id_coche int(30) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    marca text(255) NOT NULL,
    modelo text(255) NOT NULL,
    anio int(4)  NOT NULL);

CREATE TABLE fallas( 
    id_falla int(30) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    codigo_falla varchar(6) NOT NULL,
    descripcion text(255) NOT NULL,
    causa text(255) NOT NULL,
    imagen varchar(50)  NOT NULL,
    id_coche int(30) NOT NULL,
    FOREIGN KEY (id_coche) references coche(id_coche)
    );

INSERT INTO coche(marca,modelo,anio)
VALUES ('VolksWagen','Jetta','2018'),
('VolksWagen','Golf','2003'),
('VolksWagen','Polo','2019');

INSERT INTO fallas(codigo_falla,descripcion,causa,imagen,id_coche)
VALUES ('P0102','Lo que significa que el sensor MAF o en su circuito, existe una condición baja de aire','Puede haber fugas de aire, El Sensor de Flujo de Masa de Aire (MAF) puede estar contaminado o sucio.','maf_p0102','1'),
('P0103','indica que existe una condición alta en el sensor MAF o en su circuito, la entrada de aire es alta ','Sensor MAF defectuoso, Sensor de flujo de masa de aire (MAF) puede presentar problemas como cables desgastados o corroídos.','maf_p0102','1');

INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'salva'@'localhost' IDENTIFIED BY 'salva.2019';
GRANT ALL PRIVILEGES ON salva.* TO 'salva'@'localhost';
FLUSH PRIVILEGES;
