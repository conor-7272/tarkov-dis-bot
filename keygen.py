import random
import sys
from datetime import datetime
from datetime import timedelta
import sqlite3

start_date = datetime.now()
x = 0
y = 0
count = 0

try:
    conn = sqlite3.connect('userinfo.db')
    print("Opened database successfully!")
except Exception as e:
    print("Error during connection!",str(e))
c = conn.cursor()
    
def createKey(count):
        seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        for i in range(1):
            serial_key = '-'.join(''.join(random.choice(seq) for _ in range(5)) for _ in range(5))
        return serial_key

def addTime(x):
        x = int(input("Enter amount of days key will be active for: \n"))
        totalDays = start_date + timedelta(days=x)
        finish_date = totalDays
        return finish_date

def info_entry(x,y):
        finish_date = x
        serial_key = y
        c.execute("INSERT INTO stock_keys (start_date, finish_date, serial_key) VALUES (?, ?, ?)",
                 (start_date, finish_date, serial_key))
        conn.commit() 
        return info_entry


print(createKey(1))
print(addTime(1))
info_entry(x,y)
conn.close()

