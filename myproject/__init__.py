from __future__ import absolute_import, unicode_literals
import pymysql
pymysql.install_as_MySQLdb()



# Load Celery on Django startup
from .celery import app as celery_app

__all__ = ['celery_app']
