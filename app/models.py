from django.db import models
from django import forms

class EmailDatabase(models.Model):
	email = models.EmailField(blank=True)
	password = models.CharField(max_length=50)

	def __str__(self):
		return str(self.email)
