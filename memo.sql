CREATE USER etlv2 identified by "andria" ;

GRANT ALL PRIVILEGES TO ETLV2;

GRANT SELECT, INSERT, UPDATE, DELETE on Schemas.ETLV2 to ETLV2 ;

grant create session to ETLV2;
 
GRANT UNLIMITED TABLESPACE TO ETLV2 ;

GRANT ANY PRIVILEGE to ETLV2 ;

create table example (ex1 varchar(400), ex2 integer) ;