CREATE DATABASE IF NOT EXISTS db_clickhouse;
CREATE USER IF NOT EXISTS fosa DEFAULT ROLE ALL;
GRANT ALL ON db_clickhouse.* TO fosa WITH GRANT OPTION;
