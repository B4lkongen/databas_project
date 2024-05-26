DELIMITER //

CREATE TRIGGER registration_insert_grade
AFTER INSERT ON registrations
FOR EACH ROW
BEGIN
    INSERT INTO grades (assignmentId, userId, grade)
    SELECT assignmentId, NEW.userId, 0
    FROM assignments
    WHERE courseId = NEW.courseId;
END //

DELIMITER ;