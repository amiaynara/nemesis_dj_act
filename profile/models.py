#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:04:16 2019

@author: sambhav
"""

import uuid
from django.db import models
from user.models import User


class UserProfile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"
