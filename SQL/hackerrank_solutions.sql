-- author   : Enes Çavuş
-- subject  : Some of my hackerrank SQL database and query practices with MySQL
-- date     : 2021

-- my solution for https://www.hackerrank.com/challenges/the-report/problem

select IF (grades.grade > 7, students.name, NULL ), grades.grade, students.marks
from students
join grades
ON students.marks between grades.min_mark and grades.max_mark
ORDER BY grade DESC, name;


-- my solution for https://www.hackerrank.com/challenges/the-pads/problem
SELECT CONCAT(Name , "(", LEFT(Occupation,1), ")") AS ''
FROM OCCUPATIONS
ORDER BY Name;

SELECT CONCAT("There are a total of ", COUNT(Occupation), " ", LOWER(Occupation),"s.")
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation), Occupation;

-- my solution for https://www.hackerrank.com/challenges/weather-observation-station-18/problem
SELECT ROUND((MAX(LAT_N) - MIN(LAT_N)) + (MAX(LONG_W) - MIN(LONG_W)),4)
FROM STATION;

-- my solution for https://www.hackerrank.com/challenges/weather-observation-station-19/problem
SELECT ROUND(
    SQRT(
        POWER(
            ABS(MAX(LAT_N)-MIN(LAT_N)),2) + POWER(ABS(MAX(LONG_W)-MIN(LONG_W))
                                                  ,2)
    ),
    4)
FROM STATION;

-- my solution for https://www.hackerrank.com/challenges/binary-search-tree-1/problem
SELECT N,
(
    CASE
        WHEN N + 1 = P THEN "Leaf"
        WHEN N - 1 = P THEN "Leaf"
        WHEN N + 1 <> P THEN "Inner"
        WHEN N - 1 <> P THEN "Inner"
        WHEN P IS NULL THEN "Root"
    END
)
FROM BST
ORDER BY N;

-- End of this session