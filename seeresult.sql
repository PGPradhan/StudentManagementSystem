use student;
delimiter $$
drop procedure if exists seeresult $$
CREATE PROCEDURE seeresult(
	IN rono INT)
BEGIN
    SELECT * 
    FROM studentmarks
	WHERE rno = rono;

end $$
delimiter ;