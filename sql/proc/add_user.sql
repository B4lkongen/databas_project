CREATE DEFINER=`findus`@`192.120.12.220` PROCEDURE `add_user`(IN fName VARCHAR(50), OUT ret BOOL)
BEGIN
DECLARE x BOOL;
DECLARE counter INT;
DECLARE uName VARCHAR(50);
SET x = FALSE;
SET counter = 0;
WHILE (!x) DO
	SET uName = concat(fName, counter);
    IF NOT EXISTS(SELECT 1 FROM users WHERE userName = uName)THEN
	SET x = TRUE;
    END IF;
    SET counter = counter + 1;
END WHILE;
INSERT INTO users (userFName, userName) VALUES (fName, uName);
END