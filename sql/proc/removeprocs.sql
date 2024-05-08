DELIMITER //
CREATE PROCEDURE remove_user(IN uName VARCHAR(50)) -- ta bort en användare
BEGIN
    DELETE FROM grades
    WHERE userId IN (SELECT userId FROM users WHERE userName = uName);
    DELETE FROM registrations
    WHERE userId IN (SELECT userId FROM users WHERE userName = uName);
    DELETE FROM users
    WHERE userName = uName;
END //

DELIMITER ;


DELIMITER //
CREATE PROCEDURE remove_teacher(IN uName VARCHAR(50)) -- ta bort en teacher användare (lämnar kursen kvar men utan en lärare)
BEGIN
    UPDATE courses
    SET teacherId = NULL
    WHERE userId IN (SELECT userId FROM users WHERE userName = uName);
    DELETE FROM users
    WHERE userName = uName;
END //

DELIMITER ;


DELIMITER //
CREATE PROCEDURE remove_course(IN cName VARCHAR(50)) -- ta bort en kurs
BEGIN

    DECLARE cID INT;

    SELECT courseId INTO cID 
    FROM courses 
    WHERE courseName = cName;

    DELETE FROM registrations WHERE courseId = cID;

    DELETE FROM grades WHERE assignmentId IN (SELECT assignmentId FROM assignments WHERE courseId = cID);

    DELETE FROM assignments WHERE courseId = cID;

    DELETE from courses WHERE courseName = cName;

END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE remove_grade(IN aName VARCHAR(50),IN uName VARCHAR(50)) -- ta bort en grade
BEGIN

    DECLARE aID INT;
    DECLARE usID INT;

    SELECT assignmentId INTO aID
    FROM assignments
    WHERE assignmentName = aName;

    SELECT userId INTO usID
    FROM users
    WHERE userName = uName;

    DELETE FROM grades
    WHERE assignmentId = aID
    AND userId = usID;

END //

DELIMITER ;


DELIMITER //
CREATE PROCEDURE remove_assignment(IN aName VARCHAR(50)) -- ta bort en assignment
BEGIN
    DECLARE aID INT;

    SELECT assignmentId INTO aID
    FROM assignments
    WHERE assignmentName = aName;

    DELETE FROM grades
    WHERE assignmentId = aID;

    DELETE FROM assignments
    WHERE assignmentName = aName;

END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE remove_registration(IN cName VARCHAR(50),IN uName VARCHAR(50)) -- ta bort en registration från kurs
BEGIN
    DECLARE usID INT;
    DECLARE cID INT;

    SELECT userId INTO usID
    FROM users
    WHERE userName = uName;

    SELECT courseId INTO cID
    FROM courses
    WHERE courseName = cName;

    DELETE FROM registrations
    WHERE courseId = cID
    AND userId = usID;

END //

DELIMITER ;
