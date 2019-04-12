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
    anio int(4)  NOT NULL,
    codigo_falla varchar(6) NOT NULL,
    FOREIGN KEY(codigo_falla) references fallas(codigo_falla));

CREATE TABLE fallas( 
    codigo_falla varchar(6) NOT NULL PRIMARY KEY,
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
VALUES ('P0102','Lo que significa que el sensor MAF o en su circuito, existe una condición baja de aire','Puede haber fugas de aire, El Sensor de Flujo de Masa de Aire (MAF) puede estar contaminado o sucio.','sensor_maf.jpg','1'),
('P0103','Indica que existe una condición alta en el sensor MAF o en su circuito, la entrada de aire es alta ','Sensor MAF defectuoso, Sensor de flujo de masa de aire (MAF) puede presentar problemas como cables desgastados o corroídos.','sensor_maf2.jpg','2'),
('P0300','Nos indica que el ECM (Engine Control Module) ha detectado que uno o más cilindros que no están cumpliendo su función al momento de realizar la combustión.','*Alguna bujía está mala. *Inyector de Combustible con obstrucción o dañado. *Puede haber algún cortocircuito o está abierto el Arnés de Inyectores. *La compresión en los Cilindros es insuficiente. *Presión incorrecta del combustible.','arnes_inyectores.jpg','3'),
('P0122','Nos indica que el PCM (Powertrain Control Module) ha detectado que el voltaje del sensor TPS (Throttle Position Sensor), está por debajo del límite ya establecido.','*Es posible que el TPS (Sensor de Posición del Acelerador) no esté situado de forma segura. *Quizás un cable del circuito del TPS (Throttle Position Sensor) está defectuoso. *El sensor TPS puede estar defectuoso.','sensor_tps.jpg','4');


INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'salva'@'localhost' IDENTIFIED BY 'salva.2019';
GRANT ALL PRIVILEGES ON salva.* TO 'salva'@'localhost';
FLUSH PRIVILEGES;
