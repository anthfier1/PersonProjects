use atm; 

select * from account;

select * from accountType;

select * from accountHolder;

select * from accountNumber;

/* 	this doesnt work
		select distinct ah.firstName, ah.lastName, acc.last4SSN from account as acc, accountHolder as ah
		where acc.last4SSN = 1111; */ 
       
select firstName, lastName, balance from account
inner join accountHolder on nameID = accountHolder.id;  

select firstName, lastName, balance, accountNum, pin from account as acc
inner join accountNumber on acc.accountNumberID = accountNumber.id
inner join accountHolder on nameID = accountHolder.id; 

select * from account as acc
inner join accountNumber on acc.accountNumberID = accountNumber.id
inner join accountHolder on nameID = accountHolder.id; 

update account set pin = 1222 where accountNumberID = 6; 

update account set balance = balance - 5000 where accountNumberID = 7; 

update accountHolder set lastName = 'Georges' where id = 1;


