from django.db import models
import re
import datetime

# Need to install dateutil to use dateutil.relativedelta (for determing age in years)
# pip install python-dateutil
from dateutil.relativedelta import relativedelta


class UserManager(models.Manager):
    def basic_validator(self, postData):

        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'
        if len(postData['password']) < 8:
            errors['password_length'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['confirm_pw']:
            errors['password_confirm'] = 'Password and confirm values are different'
        if len(postData['email']) < 8:
            errors['email_length'] = 'Email cannot be empty'

        # Check for invalid email
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        result = re.match(pattern, postData['email'])
        if not result:
            errors['email'] = 'Invalid email address'

        # Check if the email is unique (not already in the database)
        existing_user = User.objects.filter(email=postData['email'])

        if existing_user:
            errors['email_exists'] = 'That email is already in our database'

        # Check for empty Birthday
        if postData['birthday'] == '':
            errors['birthday_empty'] = 'Please enter your birthday'
        else:
            # Check for valid Birthday (in the past)
            if datetime.datetime.strptime(postData['birthday'], '%Y-%m-%d') > datetime.datetime.now():
                errors['birthday_in_past'] = 'Birthday cannot be in the future'

            # Calculate time between now and users birthday (we want to know if they're at least 13 years old)
            now = datetime.datetime.now()
            user_birthday = datetime.datetime.strptime(
                postData['birthday'], '%Y-%m-%d')
            difference = relativedelta(now, user_birthday)

            # Check for user over 13
            if difference.years < 13:
                errors['user_age_gt_13'] = 'You must be at least 13 years old'

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    alias_name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
