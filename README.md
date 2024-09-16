# Meta Backend Capstone Project
This is a capstone project for the Meta Back-End Development course

# Important Information about the project
The project uses `pipenv` to manage the dependencies for the virtual environment.
- If `pipenv` is not currently installed, run the command `pip install pipenv`
- In your termainal or console, navigate to this project's root directory (contains the files `Pipfile`, `Pipfile.lock`, and this file)
- Use the command `pipenv shell` to enter the virtual environment
- Run the command `pipenv install` to install the dependencies.  

## Updating Database Settings in 'settings.py'
MySQL Database must be updated on your local device
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon', # <-- update
        'HOST': '127.0.0.1',
        'PORT': '3306',        # <-- update
        'USER': 'root',        # <-- update
        'PASSWORD': '',        # <-- update
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

## Creating Superuser
```sql
CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'django'@'localhost';
```
## Static content
The static content can be found at `127.0.0.1:8000/restaurant/`.

## Testing
There are 2 unit tests in this project that can be run by using the command: `python manage.py test tests\` .

# API's
```
'auth/users/'
'auth/token/login/
'api/menu-items/'
'api/menu-items/<int:pk>'
'restaurant/booking/tables'
'auth/token/logout/'
```
