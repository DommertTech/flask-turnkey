# Flask-TurnKey Version 0.0.1
# Migration_DB.py
# PeeWee Database Migrations

from peewee import *
from playhouse.migrate import *
from app import app, db

# Database
sql_db = SqliteDatabase('flask_turnkey.db')
migrator = SqliteMigrator(sql_db)

# Migration

title_field = CharField(null=True)
#status_field = IntegerField(null=True)

migrate(
    #migrator.add_column('some_table', 'status', status_field),
    #migrator.drop_column('some_table', 'old_column'),
    #migrator.rename_column('story', 'pub_date', 'publish_date'),
    #migrator.drop_not_null('story', 'pub_date'),
    #migrator.add_not_null('story', 'modified_date'),
    #migrator.rename_table('story', 'stories_tbl'),
)