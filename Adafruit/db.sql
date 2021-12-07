create database ADADB
use ADADB

CREATE TABLE Persons(
    Id int NOT NULL IDENTITY(1,1),
    Name varchar(255),
    tk varchar(255),
	mk int,
	Room int,
    PRIMARY KEY (Id),
);

INSERT INTO Persons (Name,tk,mk,Room)
VALUES 
('Cardinal','tk1','123456','1'),
('Stavanger','tk2','123456','1'),
('Norway','tk3','123456','3'),
('Vecarinal','tk4','123456','4'),
('Eva','tk5','123456','5'),
('GAbribel','tk6','123456','1'),
('Jesscica','tk7','123456','2'),
('Nova Otbu','tk8','123456','3'),
('Robinson','tk9','123456','4'),
('Mark robert','tk10','123456','5');

CREATE TABLE Room(
    Id int NOT NULL IDENTITY(1,1),
    Room varchar(255),
	fans int default 1,
	lights int default 1,
	temp int default 25,
    PRIMARY KEY (Id),
);

INSERT INTO Room (Room,fans,lights)
VALUES 
('1','3','2'),
('2','3','1'),
('3','1','3'),
('4','2','2'),
('5','1','1')