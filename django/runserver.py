import os
import sys
import subprocess

# Add the virtual environment's Python interpreter to the path
VENV_DIR = os.path.join(os.path.dirname(__file__), 'venv')
VENV_BIN_DIR = os.path.join(VENV_DIR, 'Scripts' if sys.platform == 'win32' else 'bin')
INTERP = os.path.join(VENV_BIN_DIR, 'python')

# print(sys.executable)
# print("gappp")
# print(INTERP)

# Launch the Python interpreter
# if sys.executable != INTERP:
#     args = [os.path.join(VENV_BIN_DIR, 'python'), *sys.argv]
#     subprocess.Popen(args)
#     sys.exit()

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# Run the development server
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'runserver'])
