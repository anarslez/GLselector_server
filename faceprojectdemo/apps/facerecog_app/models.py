from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email"
        if len(User.objects.filter(email = postData['email'])) > 0:
            errors["email"] = "Contact for information on this account 555 - 6767"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(User.objects.filter(email = postData['email'])) == 0:
            errors["email"] = "Invalid Login Email"
        elif not bcrypt.checkpw(postData['password'].encode(), User.objects.get(email = postData['email']).password.encode()):
            errors["password"] = "Invalid Login Password"
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.password)

class Face(models.Model):
    chin_angle = models.FloatField()
    mofa_ratio = models.FloatField()
    hlmo_angle = models.FloatField()
    shape = models.CharField(max_length=200)
    image = models.TextField()
    user = models.ForeignKey(User, related_name = "faces")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Face object: {} {} {} {} {} {}>".format(self.chin_angle, self.mofa_ratio, self.hlmo_angle, self.shape, self.image, self.user)