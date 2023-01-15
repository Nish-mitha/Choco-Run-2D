CREATE TABLE player (
    id int NOT NULL AUTO_INCREMENT,
    Player_name varchar(255),
    score int,
    PRIMARY KEY (id)
);

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT,
    Player_name varchar(255),
    Password varchar(255),
    name varchar(255),
    PRIMARY KEY (id)
);