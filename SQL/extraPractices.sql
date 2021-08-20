-- author   : Enes Çavuş
-- subject  : SQL MORE and MORE query practices with MySQL
-- date     : July 2021

-- son 4 recordu getir https://sqlbolt.com/lesson/filtering_sorting_query_results

SELECT  title FROM movies
ORDER BY year DESC
LIMIT 4;

-- ilk 5 film
SELECT  title FROM movies
ORDER BY title
LIMIT 5 ;

-- sonraki 5 film 5 inciden 10 uncuya kadar yani offset nereden başlayacağını belirtiyor.
SELECT  title FROM movies
ORDER BY title
LIMIT 5 OFFSET 5;

-- https://sqlbolt.com/lesson/select_queries_review  reference
-- List all the Canadian cities and their populations ✓
-- Order all the cities in the United States by their latitude from north to south ✓
-- List all the cities west of Chicago, ordered from west to east ✓
-- List the two largest cities in Mexico (by population) ✓
-- List the third and fourth largest cities (by population) in the United States and their population ✓

SELECT * 
FROM North_American_Cities
WHERE Country = "United States"
ORDER BY population DESC
LIMIT 2 OFFSET 2;

-- solutions for https://sqlbolt.com/lesson/select_queries_with_joins

SELECT movies.title, Boxoffice.Domestic_sales, Boxoffice.international_sales
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id;

SELECT movies.title, Boxoffice.Domestic_sales, Boxoffice.international_sales
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
WHERE Domestic_sales < international_sales;

SELECT movies.title, Boxoffice.rating
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
ORDER BY boxoffice.rating DESC;

-- solutions for https://sqlbolt.com/lesson/select_queries_with_outer_joins

SELECT DISTINCT Buildings.Building_name
FROM employees
INNER JOIN Buildings
ON Buildings.Building_name = employees.building;

SELECT DISTINCT building_name, role 
FROM buildings 
LEFT JOIN employees
ON building = building_name;

-- solution for https://sqlbolt.com/lesson/select_queries_with_nulls

SELECT name, role 
FROM employees
WHERE Building IS NULL;

-- solution for https://sqlbolt.com/lesson/select_queries_with_expressions

SELECT title, (Domestic_sales + International_sales)/1000000 as combined
FROM movies
INNER JOIN boxoffice
ON id=Movie_id;

SELECT title, (rating)*10 as percentage
FROM movies
INNER JOIN boxoffice
ON id=Movie_id;

SELECT title 
FROM movies
INNER JOIN boxoffice
ON id=Movie_id
WHERE year % 2 = 0;

-- 17 -- https://sqlbolt.com/lesson/select_queries_with_aggregates_pt_2

select role, count(role)
from employees
WHERE role = "Artist";

select role, count(role)
from employees
GROUP BY role;

select role, sum(years_employed)
from employees
WHERE role = "Engineer";    


-- order of queries  --- https://sqlbolt.com/lesson/select_queries_order_of_execution 

-- **** this is extremely important

-- SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
-- FROM mytable
--     JOIN another_table
--       ON mytable.column = another_table.column
--     WHERE constraint_expression
--     GROUP BY column
--     HAVING constraint_expression
--     ORDER BY column ASC/DESC
--     LIMIT count OFFSET COUNT;


SELECT *, count(title) as directormoveiCount FROM movies
GROUP BY director;

SELECT *, sum(domestic_sales + international_sales) FROM movies
INNER JOIN boxoffice
ON id = movie_id
GROUP BY director;


 -- https://sqlbolt.com/lesson/inserting_rows

 INSERT INTO Movies
VALUES (21,"Toy Story 4", "John Lasseter", 2015,90);

INSERT INTO boxoffice
VALUES (21, 8.7, 340, 270);

-- https://sqlbolt.com/lesson/updating_rows

UPDATE movies
SET director = "John Lasseter"
WHERE title = "A Bug's Life";

UPDATE movies
SET year = 1999
WHERE title = "Toy Story 2";

UPDATE movies
SET title = "Toy Story 3", director = "Lee Unkrich"
WHERE title = "Toy Story 8";

-- https://sqlbolt.com/lesson/deleting_rows

DELETE FROM movies
WHERE year < 2005;

DELETE FROM movies
WHERE director = "Andrew Stanton";

-- https://sqlbolt.com/lesson/creating_tables 18

    CREATE TABLE Database (
    Name VARCHAR(50),
    Version FLOAT,
    Download_count INT
);

-- ALTER TABLE - this is USEFULL , reCheck the link https://sqlbolt.com/lesson/altering_tables

ALTER TABLE Movies
ADD Aspect_ratio FLOAT;

ALTER TABLE Movies
ADD Language VARCHAR(50) DEFAULT 'English';

-- Drop -- https://sqlbolt.com/lesson/dropping_tables

DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Boxoffice;

-- END OF THE COURSE 
