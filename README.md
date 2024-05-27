# databas_project
Adrian Adborn, Viktor Listi

--------------------------------------------------------------------
Prereqesits:
Python inqierer - for user interface
https://github.com/magmax/python-inquirer

Mysql connector - for main program to talk to the sql database
https://www.mysql.com/products/connector/

Mysql database

--------------------------------------------------------------------
Installtion of the Project:

Replace in the databasedump.sql file all ocurenses of localhost with the ip of the computer wich runs the sql database.
Replace in the sql.py file all ocurenses of localhost with the ip of the computer wich runs the database, also change the password and user on line 8.

Running the databasedump.sql file should be run in the database by a privleged user which should setup the whole database.

-------------------------------------------------------------------
To login and use the application a admin user needs to be created in the sql database, the admin can then login through the application with their acronym and create other users.
