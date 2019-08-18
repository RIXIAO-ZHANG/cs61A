SELECT s1.name, s2.name
FROM students AS s1 , students AS s2
WHERE s1.name > s2.name and s1.major == s2.major;
