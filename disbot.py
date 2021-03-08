import discord
import digitalocean
import json
import requests
import sqlite3
import time 
import datetime
from switchcase import switch


client = discord.Client()
serial_waiting_list = []
serial_key = 0
ip_address_list = []
ip = 0
mytime = 0
date = 0
username = 0




try:
    conn = sqlite3.connect('userinfo.db')
    print("Opened database successfully!")
except Exception as e:
    print("Error during connection!",str(e))
c = conn.cursor()




@client.event
async def on_ready():
    print('Walter Activated'.format(client))

@client.event
async def on_message(message1):
    if message1.author in serial_waiting_list:
        serial_key = message1.content
        print(serial_key)
        serial_waiting_list.remove(message1.author)
        await message1.channel.send('Serial key being checked with database!')
        info_entry(serial_key)
    if message1.content == '!activate':
        serial_waiting_list.append(message1.author)
        await message1.channel.send('What is your serial key?')



        
    if message1.author in ip_address_list:
        ip = message1.content
        print(ip)
        ip_address_list.remove(message1.author)
        await message1.channel.send('Ip Address has been added to database!')
        info_entry(ip)
    if message1.content == '!ip-address':
        ip_address_list.append(message1.author)
        await message1.channel.send('What is your ip address? https://www.ipchicken.com/ (ip Address is needed for radar to work)')



def info_entry(x, y):
    mytime = time.time()
    mytime = int(mytime)
    date = str(datetime.datetime.fromtimestamp(mytime).strftime('%d-%m-%Y %H:%M:%S'))
    username = "kermo"
    serial_key = x
    c.execute("INSERT INTO info (start_date, finish_date, username, serialkey, ip) VALUES (?, ?, ?, ?, ?)",
            (date, date, username, serial_key, y ))
    conn.commit()





client.run('coochieman')
conn.close()
