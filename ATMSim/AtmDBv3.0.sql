DROP SCHEMA IF EXISTS atm;
CREATE SCHEMA atm; 
use atm; 

CREATE TABLE `accountType`(
	id int not null primary key, 
	accountType varchar(20) not null
);

CREATE TABLE `accountHolder`(
	id int auto_increment primary key,
	firstName varchar(20) not null,
	lastName varchar(20) not null
);

create table `accountNumber`(
	id int auto_increment primary key,
    accountNum int(6) not null unique,
    check (length(accountNum) <=> 6)
    
);

CREATE TABLE `account`(
	id int AUTO_INCREMENT primary key, 
	nameID int, 
    accountNumberID int,
	balance int unsigned not null,
	pin int(4) not null,
	typeID int(1) not null,
    last4SSN int(4) not null,
	lastUpdated timestamp default CURRENT_TIMESTAMP on UPDATE CURRENT_TIMESTAMP,
    check (length(pin) <=> 4),
    check (length(Last4SSN) <=> 4),
    FOREIGN KEY (typeID)
        REFERENCES accountType(id)
        ON DELETE CASCADE,
     FOREIGN KEY (nameID)
        REFERENCES accountHolder(id)
        ON DELETE CASCADE,
	FOREIGN KEY (accountNumberID)
        REFERENCES accountNumber(id)
        ON DELETE CASCADE
);



