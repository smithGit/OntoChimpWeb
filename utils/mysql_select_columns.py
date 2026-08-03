"""
utils/mysql_select_columns.py - Function to perform a select from indicated MySQL DB and
return a list of tuples.

2026-04-02 SMS for Proj1007_Vaccine as first use
2026-07-31 SMS Adapting for remote MySQL access to ontochimp-database. 

"""

from __future__ import annotations

import os
import re
from collections.abc import Sequence
from typing import Any

import mysql.connector
from mysql.connector import MySQLConnection
from config.settings_loader import settings

# Permit only ordinary SQL identifiers supplied by our own application code.
# This intentionally rejects spaces, punctuation, backticks, and SQL fragments.
_IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _validate_identifier(identifier: str) -> str:
    """Validate and quote a MySQL table or column identifier."""
    if not _IDENTIFIER_PATTERN.fullmatch(identifier):
        raise ValueError(f"Unsafe SQL identifier: {identifier!r}")

    return f"`{identifier}`"


def _get_connection() -> MySQLConnection:
    """Create a connection using Azure App Service environment variables."""
    # return mysql.connector.connect(
    #     host=os.environ["MYSQL_HOST"],
    #     port=int(os.getenv("MYSQL_PORT", "3306")),
    #     user=os.environ["MYSQL_USER"],
    #     password=os.environ["MYSQL_PASSWORD"],
    #     database=os.environ["MYSQL_DATABASE"],
    #     ssl_disabled=False,
    #     connection_timeout=15,
    # )
    return mysql.connector.connect(
        host=settings.mysql_host,
        port=settings.mysql_port,
        user=settings.mysql_user,
        password=settings.mysql_password,
        database=settings.mysql_database,
        ssl_disabled=False,
    )


def select_columns(
    table_name: str,
    column_names: Sequence[str] | None = None,
) -> list[dict[str, Any]]:
    """
    Select rows from one table.

    Args:
        table_name:
            Table to query.

        column_names:
            Columns to return. If None or empty, return all columns.

    Returns:
        Rows as dictionaries, suitable for Python and FastAPI JSON output.

    Example:
        select_columns(
            "term_model_doc",
            ["term_id", "term_norm"],
        )
    """
    # first try to get connection

    print("trying connection..........", flush=True)
    connection: MySQLConnection | None = None
    try:
        connection = _get_connection()
        # print(f"After connections, user: {settings.mysql_user}")
        print("we appear to have connection")
        print(f"connection obj: {connection}")
        return(["We appear to have connecion!!!"])
    except mysql.connector.Error as exc:
        print(f"MySQL SELECT failed: {exc}", flush=True)
        raise
#     table_sql = _validate_identifier(table_name)
#     print(f"temp done valid")
#     if column_names:
#         columns_sql = ", ".join(
#             _validate_identifier(column) for column in column_names
#         )
#     else:
#         columns_sql = "*"

#     sql_query = f"SELECT {columns_sql} FROM {table_sql}"

#     print(f"Executing query: {sql_query}", flush=True)
#     # rows = {"term_id": "t_123456789x", "term_norm": "suicde attempt"}
#     # return rows
#     connection: MySQLConnection | None = None
#     cursor = None
#     try:
#         connection = _get_connection()
#         print(f"After connections, user: {settings.mysql_user}")
#         # dictionary=True returns:
#         # {"term_id": "...", "term_norm": "..."}
#         # rather than:
#         # ("...", "...")
#         cursor = connection.cursor(dictionary=True)
#         cursor.execute(sql_query)
#         rows = cursor.fetchall()
#         print(f"Data retrieved: {len(rows)} rows", flush=True)

#         return rows

#     except mysql.connector.Error as exc:
#         print(f"MySQL SELECT failed: {exc}", flush=True)
#         raise

#     finally:
#         if cursor is not None:
#             cursor.close()

#         if connection is not None and connection.is_connected():
#             connection.close()


