use student;
delimiter $$
drop procedure if exists passcount$$
CREATE PROCEDURE passcount()
BEGIN
    SELECT COUNT(*) 
FROM studentmarks
WHERE percentage >= 40;
end $$
delimiter ;