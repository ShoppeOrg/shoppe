# Backend (python, django)

## How to run development server

*BEFORE RUNNING COMMANDS MAKE SURE THAT YOU ARE IN THE ROOT OF THE BACKEND DIRECTORY*

If you running for first time use these:

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
If you already have virtual environment installed. Only what you need is activate `venv`
and run the server.
```
source ./venv/bin/activate
python3 manage.py runserver
```

