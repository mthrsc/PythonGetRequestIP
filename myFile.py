#Simple script sending a get request to whatismyipaddress.com, and write the IP address in a file in the Google Drive folder.
#The goal of this script is to be able to connect to my VPN without having to pay for a DynDns service

import os.path
import requests
from datetime import datetime

filePath = '/share/CACHEDEV1_DATA/Public/GDrive/ip/ipFile.txt'

req = requests.get('http://ipv4bot.whatismyipaddress.com')
ip = req.text
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

final = ip + "\n\n" + "date: " + dt_string
print(final)

ipFile = open(filePath, "w+")
ipFile.write(final)
ipFile.close()
