-- author   : Enes Çavuş
-- subject  : SQL database and query practices with MySQL
-- date     : July 2021

-- this file contains a few queries of creating a company database from scratch based on this source -- https://www.mikedane.com/databases/sql/creating-company-database/
-- After creation, there are lots of more copmlex QUERY practices about this base database;

-- just a few examples of creating and manipulation data TABLES below 
-- NOTE: NOT ALL steps, just intro and most common steps									-- 6 July 2021

CREATE TABLE employee ( 
	emp_id INT PRIMARY KEY, 
	first_name VARCHAR(40), 
	last_name VARCHAR(40), 
	birth_dat DATE, 
	sex VARCHAR(1), 
	salary INT, 
	super_id INT, 
	branch_id INT );

CREATE TABLE branch ( 
	branc_id INT PRIMARY KEY, 
	branch_name VARCHAR(40), 
	mgr_id INT, 
	mgr_start_date DATE, FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL);

describe employee;
describe branch;

ALTER TABLE branch RENAME COLUMN branc_id TO branch_id;

ALTER TABLE employee ADD FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL;

-- and it goes on like that, Next step I'll be coding only the SQL queries about data management and other stuff****
-- first things first, we check the tables and data -- data won't be shown here - only queries

Show tables;

-- | branch            |
-- | branch_supplier   |
-- | client            |
-- | employee          |
-- | student           | - - this is the old one
-- | works_with  

select * from employee;
select * from branch;
select * from client;
select * from works_with;
select * from branch_supplier;

-- these tables are all connected with bunch of foreign keys 

-- More Basic Queris with complex database													-- 7 July

-- find all employees
SELECT * from employee;

-- get employee name,last name and salary who has more than 75000 salary
select first_name, last_name,salary from employee WHERE salary >= 75000;

-- get employee name,last name and salary ordered by salary;
SELECT first_name, salary FROM employee ORDER BY salary;

-- get client info
Select * from client;

-- employees name and sex ordered by sex first, name second;
SELECT first_name, sex FROM employee ORDER BY sex, first_name;

-- get the female count
select count(sex) from employee WHERE sex="F";

-- get first 5 employees;
SELECT * FROM employee LIMIt 5;

-- get first name column as Name, last_name as Surname 
-- can be done withour using AS keyword, too
SELECT first_name AS Name, last_name AS Surname FROM employee;

-- find the different gender types.  ----- DISTINCT
SELECT DISTINCT sex FROM employee;

--- FUNCTION - COMMON ONES  -- COUNT AVG SUM ADD SUB etc
-- find the count of emplouees
SELECT COUNT(*) FROM employee;

-- Female employees count born after 1965
SELECT COUNT(*) FROM employee WHERE sex = "F" AND birth_date > '1970-01-01';

-- AVERAGE salary
SELECT AVG(salary) FROM employee;

-- SUm salary
SELECT SUM(salary) FROM employee;

-- get female and male count together in a table  -- GROUP BY 
SELECT COUNT(sex), sex FROM employee GROUP BY sex;

-- get sales info for each employee -- how much they sold
SELECT emp_id, SUM(total_sales) AS Sold FROM works_with GROUP BY emp_id;

-- WILD CARDS 																			      -- July 8
-- find clients from LLC company ----LIKE keyword

SELECT *
FROM client
WHERE client_name LIKE '%LLC%';

-- branch suppliers in the label business
SELECT *
FROM branch_supplier
WHER supplier_name LIKE '%Lables%';

-- get employees born in October
SELECT * FROM employee
WHERE birth_date LIKE "%-10-%"; 
-- or 
SELECT * FROM employee
WHERE birth_date LIKE "%-10%"; 
-- or 
SELECT * FROM employee
WHERE birth_date LIKE "____-10%"; 

-- source here -> https://www.w3schools.com/sql/sql_wildcards.asp
-- %	Represents zero or more characters	bl% finds bl, black, blue, and blob
-- _	Represents a single character	h_t finds hot, hat, and hit
-- []	Represents any single character within the brackets	h[oa]t finds hot and hat, but not hit
-- ^	Represents any character not in the brackets	h[^oa]t finds hit, but not hot and hat
-- -	Represents a range of characters	c[a-b]t finds cat and cbt

-- 	UNION																					 --JULY 9 
-- combine data into a single table
-- get list of employesss and branch names from 2 different tables
 
SELECT first_name 
FROM employee
UNION									-- column counts must match
SELECT branch_name 
FROM branch;

SELECT first_name  FROM employee UNION SELECT branch_id  FROM branch -- multiple dtypes are allowed

-- get the money spent or earned by the company
SELECT SUM(salary) FROM employee
UNION
SELECT SUM(total_sales) FROM works_with;

-- JOINS --------------- *********************************** IMPORTANT ********************************** 
-- Find all branches and their manager's names  -- INNER JOIn, LEFT JOIN 

--STANDART INNER JOIN
SELECT branch.branch_name, employee.first_name 
FROM branch
JOIN employee ON employee.emp_id = branch.mgr_id;

--  branch_name | first_name |
-- +-------------+------------+
-- | Corporate   | David      |
-- | Scranton    | Michael    |
-- | Stamford    | Josh       |
-- +-------------+------------+

--LEFT JOIN
SELECT branch.branch_name, employee.first_name 
FROM branch
LEFT JOIN employee ON employee.emp_id = branch.mgr_id;

-- -------------+------------+
-- | branch_name | first_name |
-- +-------------+------------+
-- | Corporate   | David      |
-- | Scranton    | Michael    |
-- | Stamford    | Josh       |
-- | Science     | NULL       |
-- +-------------+------------+

--RIGHT JOIN
SELECT branch.branch_name, employee.first_name 
FROM branch
RIGHT JOIN employee ON employee.emp_id = branch.mgr_id;

-- +-------------+------------+
-- | branch_name | first_name |
-- +-------------+------------+
-- | Corporate   | David      |
-- | NULL        | Jan        |
-- | Scranton    | Michael    |
-- | NULL        | Angela     |
-- | NULL        | Kelly      |
-- | NULL        | Stanley    |
-- | Stamford    | Josh       |
-- | NULL        | Andy       |
-- | NULL        | Jim        |
-- +-------------+------------+
---- NESTED QUERIES 																		 -- JULY 10  

-- find employees who sold 20.000 or more to single client
-- first query
SELECT works_with.emp_id FROM works_with 
WHERE works_with.total_sales > 50000;

-- all together
SELECT employee.first_name FROM employee 
WHERE employee.emp_id 
IN ( 
	SELECT works_with.emp_id  
	FROM works_with  
	WHERE works_with.total_sales > 50000 
);

SELECT employee.first_name FROM employee WHERE employee.emp_id IN ( SELECT works_with.emp_id  FROM works_with WHERE works_with.total_sales > 30000 );

-- Find all clients handle by the employee 1022 and his branch id 
SELECT client.client_name 
FROM client 
WHERE client.branch_id IN (
	 SELECT branch.branch_id 
	 FROM branch 
	 WHERE branch.mgr_id = 102 
	 );

-- NOTE: IT'S ALWAYS GOOD TO lımit the inner query's output to 1 because it is a matter of equality =   =) 
SELECT client.client_name 
FROM client 
WHERE client.branch_id IN (
	 SELECT branch.branch_id 
	 FROM branch 
	 WHERE branch.mgr_id = 102 
	 LIMIT 1
	 );

-- +---------------------+
-- +---------------------+
-- | client_name         |
-- +---------------------+
-- | Dunmore Highschool  |
-- | Lackawana Country   |
-- | Scranton Whitepages |
-- | FedEx               |
-- +---------------------+


-- ON DELETE SET NULL & ON DELETE CASCADE 													-- July 11
-- 1-  SET NULL is setting the deleted and related value (foreign key in general ) to NULL
-- 2- SET CASCADE is setting the deleted and related data's whole ROW- whole data

select * from branch;
-- +-----------+-------------+--------+----------------+
-- | branch_id | branch_name | mgr_id | mgr_start_date |
-- +-----------+-------------+--------+----------------+
-- |         1 | Corporate   |    100 | 2006-02-09     |
-- |         2 | Scranton    |    102 | 1992-04-06     |
-- |         3 | Stamford    |    106 | 1998-02-13     |
-- |         4 | Science     |   NULL | NULL           |
-- +-----------+-------------+--------+----------------+

-- when we delete the mgr_id who is also an employee in the company with the id 100
-- new table will be like in case we set the NULL as assignin foreign key on delete value 
-- +-----------+-------------+--------+----------------+
-- | branch_id | branch_name | mgr_id | mgr_start_date |
-- +-----------+-------------+--------+----------------+
-- |         1 | Corporate   |    NULL | 2006-02-09     |
-- |         2 | Scranton    |    102 | 1992-04-06     |
-- |         3 | Stamford    |    106 | 1998-02-13     |
-- |         4 | Science     |   NULL | NULL           |
-- +-----------+-------------+--------+----------------+

-- CASE on CASCADE , the output will be like this  -- IMPORTANT - crucial usage for primary key assingments, when a value can't be NULL
-- use that where a foreign key is also a primary key in an another table
-- remember: primary keys can't be null and duplicated, they are unique, use auto_increment
-- +-----------+-------------+--------+----------------+
-- | branch_id | branch_name | mgr_id | mgr_start_date |
-- +-----------+-------------+--------+----------------+
-- |         2 | Scranton    |    102 | 1992-04-06     |
-- |         3 | Stamford    |    106 | 1998-02-13     |
-- |         4 | Science     |   NULL | NULL           |
-- +-----------+-------------+--------+----------------+

-- TRIGGERS 																				--July 12
CREATE TABLE LOG_Table (
	log_value VARCHAR(50)
);

DELIMITER ## -- this is special for mysql - I am changing thsi becaus I am going to use the standart delimiter inside the trigger
CREATE TRIGGER first_trigger BEFORE INSERT -- update,delete, or after inser delete update
	ON employee -- the table we are making changes
	FOR EACH ROW BEGIN
		INSERT INTO LOG_Table VALUES("employee changed - insert");
	END ##
DELIMITER

DELIMITER ## -- this is special for mysql - I am changing thsi becaus I am going to use the standart delimiter inside the trigger
CREATE TRIGGER second_trigger BEFORE UPDATE -- update,delete, or after inser delete update
	ON employee -- the table we are making changes
	FOR EACH ROW BEGIN
		INSERT INTO LOG_Table VALUES("employee changed - update");
	END ##
DELIMITER

-- After these operations LOG_Table will be like 
INSERT INTO employee(emp_id,first_name) VALUES (9,"Enes");

UPDATE employee
    -> SET sex = 'M'
    -> WHERE employee.first_name = 'Enes';

select * from LOG_Table;
-- +---------------------------+
-- | log_value                 |
-- +---------------------------+
-- | employee changed - insert |
-- | employee changed - update |
-- +---------------------------+

CREATE TRIGGER conditional_trigger_2  BEFORE INSERT 
ON employee 
FOR EACH ROW BEGIN 
IF NEW.sex = 'M' THEN INSERT INTO LOG_Table VALUES("employee insert - salary Male"); 
ELSEIF NEW.sex = 'F' THEN INSERT INTO LOG_Table VALUES("employee insert - salary Female"); 
END IF;
END#

-- After NEW INSERT

-- +-------------------------------+
-- | log_value                     |
-- +-------------------------------+
-- | employee changed - insert     |
-- | employee changed - update     |
-- | employee changed - insert     |
-- | employee changed - insert     |
-- | employee changed - insert     |
-- | employee insert - salary Male |
-- +-------------------------------+

-- drop trigger 
DROP TRIGGER first_trigger;

-- End of  this session

