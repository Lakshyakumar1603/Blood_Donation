create database blod;

use blod;

create table user(
id int(4) primary key,
name varchar(40));

insert into user values(1000,"PANKAJ");
insert into user values(1001,"BHAVNA");
insert into user values(1002,"KASHIS");
insert into user values(1003,"RITESH");

create table data(
sno int(11) primary key auto_increment,
name varchar(30) not null,
b_grp varchar(4) not null,
amt int(4) not null
);

insert into data values(1,"BHAVNA","A+",550);
insert into data values(2,"KASHIS","AB+",700);
insert into data values(3,"RITESH","A+",600);

create table pass(password char(5));

insert into pass values("1221");

create table localpass(
id int(5) ,
pass int(5));

insert into localpass values(1000,1000);
insert into localpass values(1001,1001);
insert into localpass values(1002,1002);
insert into localpass values(1002,1003);

create table recyclebin(
id int(5) not null,
sno integer not null,
date varchar(12) not null,
time varchar(5) not null
);


