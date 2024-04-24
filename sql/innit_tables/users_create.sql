DROP TABLE IF EXISTS users;

CREATE TABLE users(
	userId INT AUTO_INCREMENT,
    userRole VARCHAR(50) NOT NULL DEFAULT 'student',
	userFName VARCHAR(50) NOT NULL,
    userName VARCHAR(50),
	PRIMARY KEY(userId)
    );