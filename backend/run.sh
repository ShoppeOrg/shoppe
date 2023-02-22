#! /bin/bash

source ./venv/bin/activate
set -a
source .env
python3 manage.py runserver