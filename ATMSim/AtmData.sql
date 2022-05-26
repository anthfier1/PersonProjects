use atm;

INSERT into `accountType` (id, accountType) 
VALUES (1, 'Checking'), (2,'Savings'), (3, 'Credit'), (4, 'Investment');  

INSERT INTO `accountHolder` (firstName, lastName) 
VALUES('Anthony', 'Fierro');
INSERT INTO `accountNumber` (accountNum) 
VALUES(100100);
INSERT INTO `account` (nameID, accountNumberID, balance, pin, typeID, last4SSN)
VALUES(1, 1, 50000, 1123, 1, 1111);

INSERT INTO `accountHolder` (firstName, lastName) 
VALUES('Joe', 'Smith');
INSERT INTO `accountNumber` (accountNum) 
VALUES(100110);
INSERT INTO `account` (nameID, accountNumberID, balance, pin, typeID, last4SSN)
VALUES(2, 2, 50430, 1125, 1, 4657);

INSERT INTO `accountHolder` (firstName, lastName) 
VALUES('John', 'Doe');
INSERT INTO `accountNumber` (accountNum) 
VALUES(100120);
INSERT INTO `account` (nameID, accountNumberID, balance, pin, typeID, last4SSN)
VALUES(3, 3, 500654, 1124, 1, 7423);

INSERT INTO `accountHolder` (firstName, lastName) 
VALUES('Mike', 'Johnson');
INSERT INTO `accountNumber` (accountNum) 
VALUES(100130);
INSERT INTO `account` (nameID, accountNumberID, balance, pin, typeID, last4SSN)
VALUES(4, 4, 435643, 1126, 1, 2574);

INSERT INTO `accountHolder` (firstName, lastName) 
VALUES('Anthony', 'Fierro');
INSERT INTO `accountNumber` (accountNum) 
VALUES(100140);
INSERT INTO `account` (nameID, accountNumberID, balance, pin, typeID, last4SSN)
VALUES(1, 5, 543534, 1128, 2, 1111);

INSERT INTO `accountHolder` (firstName, lastName) 
VALUES('Joe', 'Smith');
INSERT INTO `accountNumber` (accountNum) 
VALUES(100160);
INSERT INTO `account` (nameID, accountNumberID, balance, pin, typeID, last4SSN)
VALUES(2, 6, 50430, 1125, 2, 4657);

INSERT INTO `accountHolder` (firstName, lastName) 
VALUES('John', 'Doe');
INSERT INTO `accountNumber` (accountNum) 
VALUES(100170);
INSERT INTO `account` (nameID, accountNumberID, balance, pin, typeID, last4SSN)
VALUES(3, 7, 500654, 1124, 3, 7423);

