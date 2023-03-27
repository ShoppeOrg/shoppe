# shoppe
Shoppe is a online jewerly store.
# [frontend](https://github.com/ShoppeOrg/shoppe/tree/main/frontend/README.md)
# [backend](https://github.com/ShoppeOrg/shoppe/tree/main/backend/README.md)
- [database scheme](#database-scheme)
- [Prerequisites](#prerequisites)
  * [Install dependencies](#install-dependecies)
  * [Run migrations](#run-migrations)
- [Run server](#run-server)
- [Admin](#admin)
- [Loading data](#loading-data)
- [Documentation](#documentation)
- [For geeks](#for-geeks)
  * [run.sh](#runsh)
- [Troubleshooting](#troubleshooting)
  * [runserver](#runserver)
## database scheme
![Shoppe (1)](https://user-images.githubusercontent.com/95351527/228049543-17139ff4-81e5-4779-9758-284b9f69f014.png)

## Prerequisites

- move to `backend` root folder
- create `.env` file inside root folder with following variables:

```
    SENDGRID_API_KEY=
    DJANGO_SECRET_KEY=
    DJANGO_DEBUG=
    PASSWORDLESS_EMAIL_NOREPLY_ADDRESS=
```
(Ask an administrator for the values)

- activate virtual environment

```
    source venv/bin/activate
```
- if virtual environment is not created yet, then follow this:

```python
    python3 -m venv venv
```

### Install dependencies
Usually, you do need install them everytime but depends on the updates, sometimes you need to return to this step

```python
    pip3 install -r requirements.txt
```
### Run migrations
Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
Usually, you do need run them everytime but depends on the updates, sometimes you need to return to this step.

```python
    python3 manage.py migrate
```

## Run server
*This is development server don't use it in production.*

Export **all** environment variables from .env file and run
```python
    python3 manage.py
```
OR

Use shortcut (recommended)

```
    source run.sh
```
If you are interested what does `run.sh` do, check [this](#runsh) out


## Admin
Admin page is located with url `http://localhost:8000/admin`

To sign in admin panel as a staff use thi credentials
```
    username: staff
    password: staff1234
```

If you want experience full-featured admin panel with full access use this credentials instead:
```
    username: demo
    password: demo1234
```
Aware of the [loading fixture](#loading-data) (data), unless you didn't, sign-in will be unavailable!

## Loading data
Normally, you need to do this only once.
```
    python3 manage.py loaddata user/fixtures/fixture.json
```
CAUTION!!!

This command will flush your database. Any changes that you made before will be unsaved.

## Documentation
```
    http://localhost:8000/docs
```
(requires internet connection)
## For geeks
### run.sh

```
    source ./venv/bin/activate
    set -a
    source .env
    set +a
    python3 manage.py runserver
```
## Troubleshooting
### Runserver
Errors arrise when run `python3 manage.py runserver` or `source run.sh`
<img width="568" alt="image" src="https://user-images.githubusercontent.com/95351527/228045033-d9ca8e90-ced0-4dd1-97f2-2528b86b690f.png">

SOLUTION:

Run migrations. See [how](#run-migrations).

