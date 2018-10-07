import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('output2.xlsx')
worksheet = workbook.add_worksheet()

conn=sqlite3.connect("Timer.db")
c=conn.cursor()
c.execute("SELECT * FROM Attend")
mysel=c.execute("SELECT * FROM Attend")
for i, row in enumerate(mysel):
    print row
    worksheet.write(i, 0, row[0])
    worksheet.write(i, 1, row[1])
workbook.close()
