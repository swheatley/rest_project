#!/usr/bin/env python

import csv
import sys
import os
import json

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
#import django
#django.setup()

from main.models import Phone




# print os.path.dirname(os.path.abspath(__file__))
dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = 'phones.json'

json_file = open('phones.json', 'r')


phones_data = json.load(json_file)

for phone in phones_data:
    print phone
    print phone['id']
    print phone['name']
    print phone['age']
    print phone['imageUrl']
    print phone['snippet']

    # slug value of phone id is created and saved
    new_phone, created = Phone.objects.get_or_create(slug=phone['id'])
    
    # new_phone.name is stored in memory right now.
    new_phone.name = phone['name']
    new_phone.age = phone['age']
    new_phone.image = phone['imageUrl']
    new_phone.snippet = phone['snippet']

    # saves to the database using new_phone.save()
    new_phone.save()

