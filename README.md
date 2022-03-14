# Social Media Blog

Social Media Blog project to fulfill the ITI Python course.

Below are some useful commands.

## Virtual Enviornments

NOTE: Please name your virtual enviornment 'venv' (without quotes) so it can get ignored by .gitignore.

```bash
virtualenv --python=/usr/bin/python3 <name_for_your_virtual_env>
source <name_of_venv>/bin/activate
```

To stop venv:

```bash
deactivate
```

## Pip package management

to load the env dependencies -

```bash
pip freeze > requirements.txt
```

To save your venv's dependencies:

```bash
pip install -r requirements.txt
```

## Django commands

to load the env dependencies -

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```

## Regarding .env

Please use the following article to use .env files:
https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f

You can use the .env-example, rename it to env locally.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SERVER IP`

`DATABASE IP`

`DATABASE NAME`

`DATABASE USERNAME`

`DATABASE PASSWORD`

`DATA BASE PORT`
