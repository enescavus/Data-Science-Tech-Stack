-- author   : Enes Çavuş
-- subject  : Some of my SQL hackerrank query practices with MySQL 
-- date     : June - July 2021

DATA TYPES --

INT
DECIMAL (m,n)
VARCHAR(length)
DATE -- Year-Month-Day
TIMESTAMP  -- Detailed Date with Hour-Min-Sec - similar to date
BLOB -- Binary Large Objects ---- images, files etc

Create tables -- 													     -- June 30

CREATE TABLE student (
	student_id INT PRIMARY KEY,
	name VARCHAR (25),
	major VARCHAR (20)
);

-- separate PRIMARY KEY 

CREATE TABLE student (
	student_id INT,
	name VARCHAR (25),
	major VARCHAR (20),
	PRIMARY KEY(student_id)
);


-- Check out the tables info with describe command

DESCRIBE student;

-- DROP The table with DROP TABLE command 
DROP TABLE student;

-- Modify table with ALTER TABLE COMMAND
ALTER TABLE student ADD newColumnName DECIMAL (3,2); 
ALTER TABLE student DROP COLUMN columnName;

---- insertion - operations - 											  -- July 1
INSERT INTO student VALUES(1,'Enes','CompSci');
SELECT * FROM student;

-- with null values - specific values
INSERT INTO student(student_id, name) VALUES(3, 'Kaan');

-- Duplicate values can't import for Primary values of course
INSERT INTO student(student_id, name) VALUES(3,'Esra');
--instead
INSERT INTO student(student_id, name) VALUES(4,'Esra');

-- How to delete data/row from table
DELETE FROM student WHERE student_id = 4;

---- CONSTRAINTS -> NOT NULL - UNIQUE - DEFAULT - AUTO_INCREMENT			-- Jul 2

-- Start from scratch to understand it better 
-- First things first drop the table;

DROP TABLE student;
 
-- NOT NULL & UNIQUE
CREATE TABLE student ( 
	student_id INT PRIMARY KEY, 
	name VARCHAR(25) NOT NULL, 
	major VARCHAR(20) UNIQUE);

INSERT INTO student VALUES(2, NULL, 'Biology');
ERROR 1048 (23000): Column 'name' cannot be null

-- OR 

INSERT INTO student VALUES(4,'Buse','CompSci');  -- Just an example , this constraint is useless in real life though
ERROR 1062 (23000): Duplicate entry 'CompSci' for key 'student.major'

-- DEFAULT 

>> CREATE TABLE student ( 
	student_id INT PRIMARY KEY, 
name VARCHAR(25) NOT NULL, 
major VARCHAR(20) DEFAULT 'unknown');
-- it adds a default value called 'unknown' to unspecified major columns
INSERT INTO student(student_id, name) VALUES(1,'Enes');

--- AUTO_INCREMENT

-- * Easy way to assign primary keys to each data in tables

INSERT INTO student(name, major) VALUES('Enes', 'Computer Science');
INSERT INTO student(name, major) VALUES('Aslı', 'Computer Science'); -- The student_id will be assigned automatically.

-- UPDATE & DELETE 
-- (UPDATE table SET things)												-- July 3

-- Let's say we want to shorten the Computer Science major to CS

UPDATE student SET major = "CS" WHERE major = "Computer Science";	 
 -- Other comparisons are like 
-- > = , <> , >, <, >= , <= like the other programming languages but NOT EQUALs is a bit different as it seems <>

-- One more quick update practice
UPDATE student
SET major = 'Bio'
WHERE major = 'Biology';

-- Let's change someone's major or name or whatever we want
UPDATE student SET major = 'Bio' WHERE student_id = 2; -- who is Aslı in that case

-- More detailed manipulations on table
UPDATE student SET major = 'Engineer' WHERE major = 'CS' OR major = 'Mechanics';


-- DELETE  -- DELETE FROM table ; -- Careful , this deletes all data in the table

DELETE FROM student WHERE student_id = 3; --who's Kenan in our case

-- BASIC QUERIS WITH SQL // ORDER BY										 -- July 4

SELECT student.name, student.major FROM student;
SELECT name, major FROM student
ORDER BY name DESC;

-- multiple ordering

SELECT *
FROM student
ORDER BY major, student_id DESC ;

-- limitní the number of ouputs 
SELECT *
FROM student
ORDER BY name
LIMIT 3;

-- more filtering

SELECT name FROM student
WHERE major = "Engineer"
ORDER BY name DESC;

-- More Complex WHere statements

SELECT name FROM student
WHERE major <> "Engineer" AND student_id > 2; 

-- IN keyword

SELECT * from student
WHERE name IN ("Enes","Can");

-- End of this session

