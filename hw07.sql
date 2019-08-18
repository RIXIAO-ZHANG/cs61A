CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name, s.size
  FROM dogs AS d , sizes AS s
  WHERE height <= max and height > min;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child
  FROM parents As p , dogs AS d
  WHERE parent == name
  ORDER BY - height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS name1 , b.child AS name2
  FROM parents AS a , parents AS b
  WHERE a.child != b.child and a.parent == b.parent;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT sibs.name1 || ' and ' || sibs.name2 || ' are ' ||  size1.size   || ' siblings'
  FROM siblings AS sibs ,  size_of_dogs AS size1 , size_of_dogs AS size2
  WHERE name1 < name2 and name1 == size1.name and name2 == size2.name and size1.size == size2.size;

-- Total size for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur , sum(height)
  FROM dogs
  WHERE fur == (SELECT fur FROM dogs GROUP BY fur having height >= (0.7*avg(height)) and  height <= (1.3*avg(height)))
  GROUP BY fur;
