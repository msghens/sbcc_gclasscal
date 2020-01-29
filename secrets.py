# -*- coding: utf-8 -*-
import  configparser
import os
import base64

from cryptography.fernet import Fernet


config = configparser.ConfigParser()
config.read(os.path.expanduser('~/gcal.ini'))

f = Fernet(config['DEFAULT']['key'].encode('ASCII'))

user = f.decrypt(config['gcal']['username'].encode('ASCII')).decode('ASCII')
passwd = f.decrypt(config['gcal']['passwd'].encode('ASCII')).decode('ASCII')
host = f.decrypt(config['gcal']['host'].encode('ASCII')).decode('ASCII')
port = f.decrypt(config['gcal']['port'].encode('ASCII')).decode('ASCII')
sid = f.decrypt(config['gcal']['sid'].encode('ASCII')).decode('ASCII')


# print(user)
# print(passwd)
# print(host)
# print(port)
# print(sid)