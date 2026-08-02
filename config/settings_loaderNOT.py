"""
utils.settings_loader.py - module to handle settings:
Local settings contain confidential information
settings are in effect from local, private settings
"""

import os
import local_settings as local

def settings_loader():
  print(f"Local: {local}")
  try:
      
      MYSQL_HOST = local.MYSQL_HOST
      MYSQL_PORT = local.MYSQL_PORT
      MYSQL_USER = local.MYSQL_USER
      MYSQL_PASSWORD = local.MYSQL_PASSWORD
      MYSQL_DATABASE = local.MYSQL_DATABASE

      print("Using local_settings.py")

  except ImportError:

      MYSQL_HOST = os.environ["MYSQL_HOST"]
      MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
      MYSQL_USER = os.environ["MYSQL_USER"]
      MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
      MYSQL_DATABASE = os.environ["MYSQL_DATABASE"]

      print("Using Azure environment variables")
