import os
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

def load_config(config_path: str) -> Dict:
    config = {}
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = {key: value for key, value in [line.split('=') for line in f.readlines()] if '=' in line}
    return config

def flatten_dict(nested_dict: Dict, prefix: str = '') -> Dict:
    flat_dict = {}
    for key, value in nested_dict.items():
        new_key = f'{prefix}{key}' if prefix else key
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, new_key + '.'))
        else:
            flat_dict[new_key] = value
    return flat_dict

def validate_ssh_config(config: Dict) -> List[str]:
    errors = []
    if 'username' not in config or not config['username']:
        errors.append('Missing or empty username')
    if 'password' not in config or not config['password']:
        errors.append('Missing or empty password')
    if 'host' not in config or not config['host']:
        errors.append('Missing or empty host')
    return errors

def get_sorted_files(directory: str, extension: str) -> List[str]:
    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    return sorted(files)

def get_last_modified_file(directory: str) -> str:
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return max(files, key=os.path.getmtime)