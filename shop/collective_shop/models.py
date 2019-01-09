# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

class Order(TimeStampedModel):
	user = models.ForeignKey(User)
	phone = models.TextField(default=0)
	address = models.TextField()
	PIN = models.TextField(default=0)
	url = models.URLField()
	purchased = models.BooleanField(default=False)
	flag = models.IntegerField(default=0)

class Package(TimeStampedModel):
	no_of_orders = models.IntegerField(default=0)
	total_price = models.IntegerField()
	order_date = models.DateTimeField()

	