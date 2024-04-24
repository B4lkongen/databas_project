CREATE DEFINER=`findus`@`192.120.12.220` PROCEDURE `add_course`(IN tName VARCHAR(50),
								IN cName VARCHAR(50),
								IN cHp INT,
                                OUT ret INT)
BEGIN
INSERT INTO courses (teacherId, courseName, hp)
VALUES (tName, cName, cHp);
END