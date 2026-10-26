# main.py




import os
import sys
from django.core.management import execute_from_command_line
# import subprocess
# import psutil
def run_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "table_builder.settings")
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    run_django()