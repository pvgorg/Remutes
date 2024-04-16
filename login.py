#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os, os.path, random
from pyrogram import Client, filters
os.system('clear')


if not os.path.isdir('sessions') : os.mkdir('sessions')

def app_info() :
    with open('app_info.txt', 'r') as file :
        return random.choice(file.read().split('\n')).split()

session = input('> Please enter the account number : ').replace('+', '').replace(' ', '')
if os.path.isfile(f'sessions/{session}.session') : exit('Account already exists')

info = app_info()
app = Client(
    f'sessions/{session}',
    api_id = info[1],
    api_hash = info[0]
).start()

os.system('clear')
print('account added')

app.stop()
