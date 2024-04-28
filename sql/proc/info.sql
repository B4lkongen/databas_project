DELIMITER //
CREATE PROCEDURE user_info(IN uName VARCHAR(50)) -- Hämta all information om en user (INPUT - UserName)
BEGIN
    SELECT * FROM users WHERE userName = uName;
END //

DELIMITER ;


DELIMITER //
CREATE PROCEDURE registrations_course(IN CourseName VARCHAR(50)) --Hämta alla registrations för en course (INPUT = COURSENAME)
BEGIN
    SELECT registrations.registrationId, registrations.userId 
    FROM registrations
    INNER JOIN courses ON registrations.courseId = courses.courseId
    WHERE courses.courseName = CourseName;
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE courses_all() --Hämta alla kurser som existerar (OUTPUT - NAMN, HP)
BEGIN
    SELECT courses.courseName, courses.hp FROM courses;
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE course_info(IN CourseName VARCHAR(50)) -- Hämta info om specifik kurs
BEGIN
    SELECT courses.courseName, courses.hp 
    FROM courses
    WHERE courses.courseName = CourseName; -- fixa så denna hämtar teacher namnet också
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE courses_teacher(IN teacherName VARCHAR(50)) -- Hämta alla kurser utlärda av specifik lärare
BEGIN
    --Inte klar

END //

DELIMITER ;