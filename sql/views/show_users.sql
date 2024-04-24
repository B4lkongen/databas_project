CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `findus`@`192.120.12.220` 
    SQL SECURITY DEFINER
VIEW `show_users` AS
    SELECT 
        `users`.`userFName` AS `userFName`,
        `users`.`userRole` AS `userRole`,
        `users`.`userName` AS `userName`
    FROM
        `users`