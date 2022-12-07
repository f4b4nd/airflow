 Identifier 'dag_run_dag_id_execution_date_key' exceeds maximum length of 30 characters

# 1. create table "connection" : password VARCHAR2(500 CHAR) instead of 5000
# 2. create table "dag_run" : remove: CONSTRAINT dag_run_dag_id_execution_date_key UNIQUE (dag_id, execution_date),
# 3. create table "sla_miss": remove: CONSTRAINT sla_miss_pkey PRIMARY KEY (task_id, dag_id, execution_date)
# 5. create table "session" : ajout de guillemets


# 6. site-packages/alembic/runtime/migration.py : _insert_version() 
# 4. jaydebeapi --> autocommit=false (modif dans jaydebeapi) + ligne 535 execute _handle_sql_exception
# 5. site-packages/sqlalchemy/engine/cursor.py --> _we_dont_return_rows


Créer une procédure sql :
- 1) lancer le script sql avec la syntaxe procédure
- 2) la procédure a été compilée, la réouvrir dans l'onglet "procédures"
- 3) lancer la procédure
- 4) la recompiler directement dans la procédure si besoin