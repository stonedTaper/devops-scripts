#!/usr/bin/env python3

import os
import sys
import pathlib

# Get the absolute path to the directory containing the script
script_dir = pathlib.Path(__file__).parent.absolute()

# Create a virtual environment in the script's directory if it doesn't exist
venv_path = os.path.join(script_dir, 'venv')
if not os.path.exists(venv_path):
    sys.exit(f"Creating virtual environment at {venv_path}")
    os.system(f"python3 -m venv {venv_path}")

# Activate the virtual environment
os.system(f"source {venv_path}/bin/activate")

# Install dependencies from requirements.txt
requirements_path = os.path.join(script_dir, 'requirements.txt')
if os.path.exists(requirements_path):
    os.system(f"pip install -r {requirements_path}")

# Run the main script
sys.path.insert(0, script_dir)
from main import run
run()