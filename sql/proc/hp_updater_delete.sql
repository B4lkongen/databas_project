CREATE TRIGGER hp_updater_delete
AFTER DELETE ON assignments
FOR EACH ROW
UPDATE courses
SET courses.hp = (SELECT SUM(assignments.hp) FROM assignments WHERE courseId = OLD.courseId)
WHERE courseId = OLD.courseId;