create user artikli identified by ftn
	default tablespace USERS temporary tablespace TEMP;

	

	grant connect, resource to artikli;

	grant create table to artikli;

	grant create view to artikli;

	grant create procedure to artikli;

	grant create synonym to artikli;

	grant create sequence to artikli;

	grant select on dba_rollback_segs to artikli;

	grant select on dba_segments to artikli;

	grant unlimited tablespace to artikli;