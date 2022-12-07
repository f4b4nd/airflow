

CREATE TABLE sla_miss (
        task_id VARCHAR2(250 CHAR) NOT NULL, 
        dag_id VARCHAR2(250 CHAR) NOT NULL, 
        execution_date varchar2(200), 
        email_sent SMALLINT, 
        timestamp TIMESTAMP WITH TIME ZONE, 
        description CLOB, 
        notification_sent SMALLINT
        , CONSTRAINT sla_miss_pkey PRIMARY KEY (task_id, dag_id, execution_date) 
)


/*
CREATE OR REPLACE PROCEDURE 
INSERT_TEST	
IS 
	local_var varchar2(400) ;
BEGIN
	INSERT INTO alembic_version (version_num) VALUES ('90244fb8b83') RETURNING alembic_version.version_num INTO local_var;
END;


INSERT INTO alembic_version (version_num) VALUES ('290244fb8b83') RETURNING alembic_version.version_num INTO local_var

select * from connection

INSERT INTO connection (conn_id, conn_type, description, host, schema, login, password, port, is_encrypted, is_extra_encrypted, extra) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) RETURNING connection.id INTO ?



insert INTO alembic_version (version_num) VALUES ('290244fb8b83')

CREATE TABLE etlv2."SESSION" (
        id INTEGER NOT NULL, 
        session_id VARCHAR2(255 CHAR), 
        data BLOB, 
        expiry DATE, 
        PRIMARY KEY (id), 
        UNIQUE (session_id)
)


CREATE TABLE sla_miss (
        task_id VARCHAR2(250 CHAR) NOT NULL, 
        dag_id VARCHAR2(250 CHAR) NOT NULL, 
        execution_date TIMESTAMP WITH TIME ZONE NOT NULL, 
        email_sent SMALLINT, 
        timestamp TIMESTAMP WITH TIME ZONE, 
        description CLOB, 
        notification_sent SMALLINT
        , CONSTRAINT sla_miss_pkey PRIMARY KEY (task_id, dag_id, execution_date) 
)



CREATE TABLE dag_run (
        id INTEGER NOT NULL, 
        dag_id VARCHAR2(250 CHAR) NOT NULL, 
        queued_at TIMESTAMP WITH TIME ZONE, 
        execution_date TIMESTAMP WITH TIME ZONE NOT NULL, 
        start_date TIMESTAMP WITH TIME ZONE, 
        end_date TIMESTAMP WITH TIME ZONE, 
        state VARCHAR2(50 CHAR), 
        run_id VARCHAR2(250 CHAR) NOT NULL, 
        creating_job_id INTEGER, 
        external_trigger SMALLINT, 
        run_type VARCHAR2(50 CHAR) NOT NULL, 
        conf BLOB, 
        data_interval_start TIMESTAMP WITH TIME ZONE, 
        data_interval_end TIMESTAMP WITH TIME ZONE, 
        last_scheduling_decision TIMESTAMP WITH TIME ZONE, 
        dag_hash VARCHAR2(32 CHAR), 
        log_template_id INTEGER, 
        updated_at TIMESTAMP WITH TIME ZONE, 
        CONSTRAINT dag_run_pkey PRIMARY KEY (id), 
        CONSTRAINT dag_run_dag_id_execution_date_key UNIQUE (dag_id, execution_date), 
        CONSTRAINT dag_run_dag_id_run_id_key UNIQUE (dag_id, run_id), 
        CONSTRAINT task_instance_log_template_id_fkey FOREIGN KEY(log_template_id) REFERENCES log_template (id)
)



CREATE TABLE connection (
        id INTEGER NOT NULL, 
        conn_id VARCHAR2(250 CHAR) NOT NULL, 
        conn_type VARCHAR2(500 CHAR) NOT NULL, 
        description CLOB, 
        host VARCHAR2(500 CHAR), 
        schema VARCHAR2(500 CHAR), 
        login VARCHAR2(500 CHAR), 
        // password VARCHAR2(500 CHAR),
        port INTEGER, 
        is_encrypted SMALLINT, 
        is_extra_encrypted SMALLINT, 
        extra CLOB, 
        CONSTRAINT connection_pkey PRIMARY KEY (id), 
        CONSTRAINT connection_conn_id_uq UNIQUE (conn_id)
)


*/
