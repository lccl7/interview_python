#coding: utf-8

import re
import requests
from pprint import pprint
import urllib3

inputfile = 'station.txt'
text = ''
with open(inputfile, 'r') as infile:
    for line in infile:
        text += line
#url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955' 
#text = requests.get(url, verify=False)
#print(text)
stations = re.findall(r'([A-Z]+)\|([a-z]+)', text)
stations = dict(stations)
stations = dict(zip(stations.values(), stations.keys()))
pprint(stations, indent = 4)
