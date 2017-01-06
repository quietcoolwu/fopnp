#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search2.py

import json
from pprint import pprint

import requests


def geocode(address):
    parameters = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    pprint(answer, indent=4)
    with open('search2.json', 'w') as f:
        json.dump(answer, f, indent=4)
    print(answer['results'][0]['geometry']['location'])


if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
