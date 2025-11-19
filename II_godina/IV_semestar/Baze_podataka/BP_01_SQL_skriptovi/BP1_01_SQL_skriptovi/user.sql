create user proj identified by ftn
	default tablespace USERS temporary tablespace TEMP;

	

	grant connect, resource to proj;

	grant create table to proj;

	grant create view to proj;

	grant create procedure to proj;

	grant create synonym to proj;

	grant create sequence to proj;

	grant select on dba_rollback_segs to proj;

	grant select on dba_segments to proj;

	grant unlimited tablespace to proj;