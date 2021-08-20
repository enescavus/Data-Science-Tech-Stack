-- author   : Enes Çavuş
-- subject  : SQL database and query practices with MySQL - select, create, union, group by and more
-- date     : July 2021

-- 1 REVERSING THE SELECT QUERY 1
SELECT *
FROM CITY
WHERE 
COUNTRYCODE = 'USA'
AND
POPULATION > 100000;

-- REVERSING THE SELECT QUERY 2
SELECT NAME
FROM CITY
WHERE
POPULATION > 120000
AND
COUNTRYCODE = 'USA';

-- SELECT ALL
SELECT *
FROM CITY

-- SELECT BY ID
SELECT *
FROM CITY 
WHERE ID = 1661;


-- JAPNESE CCITIES' ATRIBUTES
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'JPN';

-- JAPANESE CITIES' NAMES
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'JPN';

-- WEATHER OBSERVATION STATION 1
SELECT CITY,STATE
FROM STATION;

-- WEATHER OBSERVATION STATION 3
-- DISTINCT EXCLUDES DUPLICATE VALUES
SELECT DISTINCT CITY 
FROM STATION
WHERE ID % 2 = 0; -- CONDITION 

-- WEATHER OBSERVATION STATION 4
SELECT COUNT(CITY) -  COUNT( DISTINCT CITY)
FROM STATION

-- WEATHER OBSERVATION STATION 5
SELECT CITY,
LENGTH(CITY) CITY_LENGTH FROM STATIONS
ORDER BY CITY_LENGTH ASC,
CITY ASC LIMIT 1;

SELECT CITY,
LENGTH(CITY) CITY_LENGTH FROM STATION
ORDER BY CITY_LENGTH DESC,
CITY DESC LIMIT 1;

-- WEATHER OBSERVATION STATION 6
SELECT DISTINCT CITY
FROM STATION
WHERE CITY LIKE "a%" or CITY LIKE "e%" or CITY LIKE "i%" or CITY LIKE "o%" or CITY LIKE "u%"

-- UNDERSTANDING CEIL - ROUND - FLOOR difference
SET @variable1 = (select AVG(REPLACE(Salary, '0' , '')) from EMPLOYEES);
SET @variable2 = (select AVG(Salary) from EMPLOYEES);
SELECT @variable2 - @variable1

--Ceil is gonna round it to the nex value 
--if it is positive goes one number higher  13.25 goes 14
--if it is negative goes one number lower  -13.25 goes 14
SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0',''))) FROM EMPLOYEES;

/* 
create a new column
do multipications 
get counts
*/
SELECT salary * months AS earnings, count(*) from Employee GROuP BY earnings ORDER BY earnings DESC LIMIT 1;

/*
SUM - ROUND 
*/
SELECT ROUND(SUM(LAT_N),2), ROUND(SUM(LONG_W),2) FROM STATION ;

/*
WHERE - SUM - ROUND 
*/
select round(sum(LAT_N),4) from STATION where LAT_N > 38.7880 AND  LAT_N < 137.2345;

/*
WHERE - MAX - ROUND 
*/
select round(max(LAT_N),4) from STATION where LAT_N < 137.2345;

/*
WHERE - ORDER BY ____ DESC - ROUND 
*/
select ROUND(LONG_W, 4) from STATION where LAT_N < 137.2345 ORDER BY LAT_N DESC LIMIT 1 ;

/*
WHERE - MIN - ROUND 
*/
select ROUND(MIN(LAT_N),4) from STATION where LAT_N > 38.7780;

/*
WHERE - ORDER BY ____ ASC - ROUND 
*/
select ROUND(LONG_W,4) from STATION where LAT_N > 38.7780 ORDER BY LAT_N ASC LIMIT 1;

/* 2 different tables operatins */
select sum(CITY.POPULATION)
from CITY, COUNTRY
where CITY.COUNTRYCODE = COUNTRY.CODE AND COUNTRY.CONTINENT = 'Turkey';

-- MORE  

select sum(CITY.POPULATION)
from CITY
inner join COUNTRY on CITY.COUNTRYCODE = COUNTRY.CODE
where COUNTRY.CONTINENT = 'Turkey' ;

select CITY.NAME
from CITY
inner join COUNTRY on COUNTRY.CODE = CITY.COUNTRYCODE
where COUNTRY.CONTINENT = 'Turkey'
;

SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY INNER JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;

-- Source : hackerrank sql https://www.hackerrank.com/domains/sql?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=sql


