#!/bin/bash

venv_dir='./env'
requirements_file='./requirements.txt'

python3 -m venv "$venv_dir"

. "$venv_dir"/bin/activate

pip install --requirement "$requirements_file"
