#Create a relational database(2tables) of your own choice. It is must be a meaningful/thought out database.
CREATE DATABASE MY_DATABASE;
USE MY_DATABASE;
DROP TABLE COURSE;
DROP TABLE student;
# Both tables must have a primary key and the correct data types.Include a minimum of 5 fields in atleast one of the tables.
CREATE TABLE student( s_id char(6) not null,s_name varchar(20) not null,s_dob date not null,s_email varchar(20),s_phone varchar(20) not null,s_address varchar(20),s_age int, primary key (s_id), unique(s_phone));
INSERT INTO student(s_id,s_name,s_dob,s_email,s_phone,s_address,s_age) values ("S001","Samuel", "2001-10-19","abc@gmail.com","07913061608","djfaskjfkasj",21),("S002","Martin","2000-08-23","dec@gmail.com","53486784323","dhjgdhjgasj",21),("S003","Max","2001-06-30","max@gmail.com","5348908123","dhkfjalkjsj",21),("S004","Tom","2001-02-17","tom@gmail.com","5387984323","dcnvzxtidhjgasj",22),("S005","Andrew","2000-04-16","and@gmail.com","55556784323","jkjioyuyghjgasj",21),("S006","Neil","2000-10-03","Neil@gmail.com","53867808793","dhjgdhjqwuiotuj",20);
# View and show both table structures and data to make sure they are set up correctly.
EXPLAIN student;
SELECT * FROM student;
CREATE TABLE  course(R_id char(8) not null primary key,s_id char(6) not null , c_name varchar(20),c_fee int,foreign key(s_id) references student(s_id));
EXPLAIN COURSE;
DROP TABLE COURSE;
ALTER TABLE course RENAME COLUMN R_id TO r_id;
# Enter records into both tables and view them.Make sure atleast one of your tables has 10 records.
INSERT INTO course(r_id,s_id,c_name,c_fee) values("R001","S002","Diploma",300),("R002","S001","Diploma",300),("R003","S003","code camp 2",300),("R004","S003","Diploma",300),("R005","S004","Diploma",300),("R006","S002","code camp1",120),("R007","S002","Diploma",300),("R008","S002","Codecamp2",100),("R009","S004","Diploma",300),("R010","S005","Codecamp1",120),("R011","S004","Code camp1",120);
SELECT * FROM course;
# Update a record
UPDATE course SET s_id="S005" where r_id="R007";
# Delete a record
DELETE FROM course where r_id="R011";
# Join tables
SELECT student.s_name,course.c_fee FROM course INNER JOIN student ON student.s_id=course.s_id;
SELECT * FROM course INNER JOIN student ON student.s_id=course.s_id;
# Run a simple query (onefield/column) searching one table.
SELECT s_name FROM student;
# Run a complex query (more than one field/column) to demonstrate the relations between the 2 tables
SELECT student.s_name,course.c_fee,course.c_name FROM student,course where student.s_id=course.s_id;
SELECT * FROM course,student WHERE student.s_id=course.s_id AND student.s_name LIKE 'A%';
# Retrieve all your data sorted in ascending order on an appropriate field (onetable)
SELECT * FROM student ORDER BY s_name ASC;
# Filter data using comparison operators (onetable)
SELECT * FROM course WHERE c_fee>120;
