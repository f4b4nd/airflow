create or replace PROCEDURE 
INSERT_TEST	
IS 
	local_var varchar2(400) ;
BEGIN
	INSERT INTO alembic_version (version_num) VALUES ('390244fb8b83') RETURNING alembic_version.version_num INTO local_var;
    dbms_output.put_line(local_var);
END;
