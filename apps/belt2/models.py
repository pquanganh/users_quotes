from __future__ import unicode_literals

from django.db import models

import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
	def regValidator(self, postData):
		errors = {}
		if User.objects.filter(email = postData['email']):
		 	errors['email_exists'] = "An account associated with that email address already exists."
		if len(postData['name']) < 3:
			errors['name'] = "Name must be at least 3 characters long."
		if len(postData['alias']) < 2:
			errors['alias'] = "Alias must be at least 2 characters long."
		if EMAIL_REGEX.match(postData['email']) == None:
			errors['email_format'] = "Email must be in valid email format."
		if len(postData['password']) < 7:
			errors['pword_length'] = "Password must be at least 7 characters long."
		if postData['password'] != postData['pwconf']:
			errors['pwconf'] = "Password confirmation must match password."
		print errors
		return errors
	def loginValidator(self, postData):
		user = User.objects.filter(email = postData['login_email'])
		errors = {}
		if not user:
			errors['email'] = "Please enter a valid email address."
		if user and not bcrypt.checkpw(postData['login_password'].encode('utf8'), user[0].password.encode('utf8')):
			errors['password'] = "Invalid password."
		return errors
class quoteManager(models.Manager):
	def addValidator(self, postData):
		errors = {}
		if len(postData['author']) < 3:
			errors['author'] = "Quoted By must be at least 3 characters long."
		if len(postData['message']) < 10:
			errors['message'] = "Message must be at least 10 characters long"
		print errors
		return errors

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	dob = models.DateTimeField(null=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = userManager()

class Quote(models.Model):
	author = models.CharField(max_length=255)
	message = models.TextField()
	uploader = models.ForeignKey(User, related_name = "uploaded_quotes")
	liked_users = models.ManyToManyField(User, related_name = "liked_quotes")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = quoteManager()






