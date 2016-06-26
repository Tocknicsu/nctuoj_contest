#!/bin/sh
PSQL="env psql"
PSQL_FILE="./../psql.sql"
DBHOST="localhost"
DBUSER="nctuoj_contest"
DBNAME="nctuoj_contest"
DBPASSWORD="nctuoj_contest"
export PGPASSWORD=${DBPASSWORD}
${PSQL} -h ${DBHOST} -d ${DBNAME} -U ${DBUSER} < ${PSQL_FILE}
unset PGPASSWORD
