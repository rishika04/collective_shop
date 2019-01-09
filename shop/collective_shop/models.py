# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

class Order(TimeStampedModel):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=50, null=True, blank=True)
	address = models.TextField()
	url = models.URLField()
	flag = models.IntegerField(default=0)

class Package(TimeStampedModel):
	no_of_orders = models.IntegerField(default=0)
	total_price = models.IntegerField()
	order_date = models.DateTimeField()

	