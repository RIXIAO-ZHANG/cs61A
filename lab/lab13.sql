.read su19data.sql

CREATE TABLE obedience AS
  SELECT students.seven , students.instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT students.time , students.smallest
  FROM students WHERE students.smallest > 2
  ORDER BY students.smallest LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT s1.pet, s1.song, s1.color, s2.color
  FROM students AS s1, students AS s2
  WHERE s1.time != s2.time and s1.time < s2.time and s1.pet = s2.pet and s1.song = s2.song;


CREATE TABLE smallest_int_having AS
  SELECT students.time , students.smallest
  FROM students GROUP BY students.smallest HAVING count(*) = 1;
