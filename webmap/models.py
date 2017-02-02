from __future__ import unicode_literals
from django.db import models
from agol.models import AGOL_Item

class Webmap_Contact(models.Model):
	contact_name = models.CharField(max_length=120)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Webmap Contact'

	def __str__(self):
		return self.contact_name

#--WEBMAP TABLE
class Webmap(models.Model):
	name = models.CharField(max_length=20)
	purpose = models.CharField(max_length=50)
	contact = models.ForeignKey(Webmap_Contact)
	collector = models.BooleanField()
	collector_offline = models.BooleanField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

#--WEBMAP APP TABLE
class Webmap_App(models.Model):
	name = models.CharField(max_length=20)
	purpose = models.CharField(max_length=50)
	url = models.URLField()
	contact = models.ForeignKey(Webmap_Contact)
	webmap = models.ForeignKey(Webmap)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Webmap App'

	def __str__(self):
		return self.name

#--AGO_WEBMAP Many2Many
class Webmap_Item(models.Model):
	name = models.CharField(max_length=120, blank=True)
	webmap = models.ManyToManyField(Webmap)
	agol_item = models.ManyToManyField(AGOL_Item)
	map_description = models.TextField(blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Webmap Item'

	def __str__(self):
		return self.name