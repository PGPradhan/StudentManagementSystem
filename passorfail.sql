
delimiter $$
drop procedure if exists passorfail $$
CREATE PROCEDURE passorfail(sid int)
BEGIN
DECLARE per int;
select percentage into per from studentmarks where rno = sid;
IF per<35 THEN select 'Fail';
ELSEIF per<50 THEN select 'C Grade';
ELSEIF per<70 THEN select 'B Grade';
ELSE select 'A Grade';
END IF;
END$$
delimiter ;