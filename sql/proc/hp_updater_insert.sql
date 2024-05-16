CREATE TRIGGER hp_updater_insert
AFTER INSERT ON assignments
FOR EACH ROW
UPDATE courses
SET courses.hp = (SELECT SUM(assignments.hp) FROM assignments WHERE courseId = NEW.courseId)
WHERE courseId = NEW.courseId;
