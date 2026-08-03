

from __future__ import annotations

import os
import re
from collections.abc import Sequence
from typing import Any

import mysql.connector
from mysql.connector import MySQLConnection
from config.settings_loader import settings


def select_columns():
    return "mysql_select_columns imported successfully"