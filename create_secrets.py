import  configparser
import os
import sys
from cryptography.fernet import Fernet
import getpass
import base64

# username = input("Username: ")
# password = getpass.getpass("Password: ")


#Fill out then clean

key = Fernet.generate_key()

config = configparser.ConfigParser()
# config.read(os.path.expanduser('~/gcal.ini'))
config['DEFAULT'] = {}
config['DEFAULT']['key'] =  key.decode("ASCII")

f = Fernet(key)

# Fill, run, clear
username = b''
passwd = b''
host = b''
port = b''
sid = b''


config['gcal'] = {}
gcal = config['gcal']
gcal['username'] = f.encrypt(username).decode('ASCII')
gcal['passwd'] = f.encrypt(passwd).decode('ASCII')
gcal['host'] = f.encrypt(host).decode('ASCII')
gcal['port'] = f.encrypt(port).decode('ASCII')
gcal['sid'] = f.encrypt(sid).decode('ASCII')

with open(os.path.expanduser('~/gcal.ini'),'w')  as configfile:
    config.write(configfile)