# CUSTOMIZED USER MODEL DJANGO

Project to highlight steps required to customize user model using django django docs https://docs.djangoproject.com/en/5.1/topics/auth/customizing/

This tutorial will make use of a fully customized user model without extending existing user model.

## Steps
- install django rest framework.
- create main project and user app for model customizations.
- create new user model with following fields:
    - username
    - email
    - password
    - is_active
    - is_staff
    - is_superuser
- Write manager for a custom user model.
- change project auth model in settings.py ```AUTH_USER_MODEL = "user.User"```.
- create migrations for user model and apply.
- add drf spectacular to test endpoints.
- create user serializer for User model with:
    - email validation.
    - additional password field for password check.
    - add other validation checks, if required.
- create user endpoints in views making use of custom Userserializer.
