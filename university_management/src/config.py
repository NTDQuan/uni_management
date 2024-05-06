# -*- encoding:utf-8 -*-
import os


global APP_PATH
# Take fixed file path, and not the relative file path
APP_PATH = os.path.dirname(os.path.realpath(__file__))

global state

global DBCONFIG

global profile

DBCONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "quanhtht123",
    "database": "uni_management"
}



state = "NOT LOGIN"

__all__ = ["APP_PATH", "DBCONFIG", "state"]

