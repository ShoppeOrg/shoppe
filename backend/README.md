# Backend (python, django)

## How to run development server

*BEFORE RUNNING COMMANDS MAKE SURE THAT YOU ARE IN THE ROOT OF THE BACKEND DIRECTORY*

### Use the script
But, be aware of having migrated data models and installed virual environment `venv`.
More [above](#if-you-running-for-first-time-use-these)

```
source run.sh
```

### TL;DR

First activate environment variables that are stored inside of `.env` file

```
set -a
source .env
set +a
```

#### If you running for first time use these
```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
If you already have virtual environment installed, consider the following steps
- activate virtual environment `venv`
- set all environment variables
- run the server
```
source ./venv/bin/activate
set -a
source .env
set +a
python3 manage.py runserver
```
