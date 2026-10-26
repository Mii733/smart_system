# utils.py
from django.db import connections

from django.db.utils import DEFAULT_DB_ALIAS, ProgrammingError




def alter_column(model, initial_field, new_field):
    with connections[model._meta.app_label].schema_editor() as editor:
        editor.alter_field(model, initial_field, new_field)