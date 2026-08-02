"""
test_mysql.py - short app to test Azure App Service MySQL db, no FastAPI

This module uses utils.select_columns to connect to Azure db, but 
does not activate any FastAPI processes in the server.


2026-07-31 SMS First MySQL connection for OntoChimpWeb - connected but not pretty

Review and delete: For 8/1:
make this test_mysql.py to do the sql within this module, w/o select_columns
copy to do test_api_module.py to implement ALL db work in module using select_columns
Find the documentation in which we defint the connection parameters pwd
try the url command in browser!  what is adddress?

Folder: cd "D:\\OntoChimpWeb"
conda activate python314   ** NOT: env_ontochimp
Execute: python -m tests.test_mysql << because we are in tests
and we need to access a sibling folder utils, executing as a module
is needed; when doing so, omit the .py suffix!!
"""

from utils.mysql_select_columns import select_columns
from config.settings_loader import settings
import os
import mysql.connector
from mysql.connector import MySQLConnection


def get_connection():
    return mysql.connector.connect(
        host=settings.mysql_host,
        port=settings.mysql_port,
        user=settings.mysql_user,
        password=settings.mysql_password,
        database=settings.mysql_database,
        ssl_disabled=False,
    )

try:
    connection = get_connection()
    print(f"have conn? {settings.mysql_user}")
    # dictionary=True returns:
    # {"term_id": "...", "term_norm": "..."}
    # rather than:
    # ("...", "...")
    cursor = connection.cursor(dictionary=True)
    sql_query = "SELECT * FROM term_model_doc"
    cursor.execute(sql_query)


    rows = cursor.fetchall()
    print(f"Data retrieved: {len(rows)} rows", flush=True)
    rows = select_columns("term_model_doc", ["term_id", "term_norm"])
    print("afte select_columns")
    for row in rows:
      print(f"row {row}")
except Exception as err:
    print(f"Error in connection: {err}")