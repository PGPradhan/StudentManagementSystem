use student;
delimiter $$
drop procedure if exists failcount$$
CREATE PROCEDURE failcount()
BEGIN
    SELECT COUNT(*) 
FROM studentmarks
WHERE percentage < 40;
end $$
delimiter ;