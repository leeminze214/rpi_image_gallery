CREATE DATABASE GREEN_BOND;

CREATE TABLE USERS(
    userid SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    password varchar(255) NOT NULL
);

CREATE TABLE DATA(
    plantid int NOT NULL,
    CONSTRAINT fk_plantid FOREIGN KEY (plantid) REFERENCES PLANTS(plantid),
    time TIMESTAMP NOT NULL,
    data_x int,
    data_y int
);

CREATE TABLE PLANTS(
    plantid SERIAL PRIMARY KEY,
    userid int,
    name varchar(255),
    CONSTRAINT fk_userid FOREIGN KEY (userid) REFERENCES users(userid) 
);