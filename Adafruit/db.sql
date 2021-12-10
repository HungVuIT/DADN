create database ADADB
use ADADB

CREATE TABLE Persons(
    id int NOT NULL IDENTITY(1,1),
    name varchar(255),
    tk varchar(255),
	mk varchar(255),
	room varchar(255),
    PRIMARY KEY (id),
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

CREATE TABLE LightHistory(
	room_id int not null,
	time_created datetime not null DEFAULT GETDATE(),
	feed_data int not null,
	CONSTRAINT fk_room_id_light
 	FOREIGN KEY (room_id)
 	REFERENCES Room (Id)
);


CREATE TABLE FanHistory(
	room_id int not null,
	time_created datetime not null DEFAULT GETDATE(),
	feed_data int not null,
	CONSTRAINT fk_room_id_fan
 	FOREIGN KEY (room_id)
 	REFERENCES Room (Id)
);

insert into LightHistory(room_id, feed_data) values (1, 1);
insert into LightHistory(room_id, feed_data) values (1, 0);
insert into LightHistory(room_id, feed_data) values (1, 2);
insert into LightHistory(room_id, feed_data) values (1, 1);
insert into LightHistory(room_id, feed_data) values (1, 0);
insert into LightHistory(room_id, feed_data) values (1, 2);
insert into LightHistory(room_id, feed_data) values (2, 1);



insert into FanHistory(room_id, feed_data) values (1, 1);
insert into FanHistory(room_id, feed_data) values (1, 0);
insert into FanHistory(room_id, feed_data) values (1, 2);
insert into FanHistory(room_id, feed_data) values (1, 1);
insert into FanHistory(room_id, feed_data) values (1, 0);
insert into FanHistory(room_id, feed_data) values (1, 2);
insert into FanHistory(room_id, feed_data) values (2, 1);

