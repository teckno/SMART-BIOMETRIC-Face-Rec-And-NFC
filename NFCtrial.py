#!/usr/bin/python
import datetime
import sqlite3
conn = sqlite3.connect('NFC.db')
import serial
de=datetime.datetime.now()

ser = serial.Serial('COM15', 9600)
another ="yes"


tag=''
while another=="yes":

while(ser.isOpen != True):
 
    d=raw_input("please enter you tag number")
    
    while len(tag) != 0:
        tag = ser.read(27)
    while len(tag) == 0:
        tag = ser.read(27)
    conn.execute("INSERT INTO Students (ID,time) VALUES ('Mwape','43543354')");

    conn.execute("INSERT INTO STUDENTS (ID,time) \
        #VALUES (?,?)",(tag,de));

    conn.execute("INSERT INTO Students (ID,time)"
    \ VALUES (?,?)" ,(tag,de));
    conn.commit()
    print tag

    another = raw_input("Input another? (yes, no, deleteLast): ")


print "Records created successfully";
conn.close()
