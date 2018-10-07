import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('output2.xlsx')
worksheet = workbook.add_worksheet()

conn=sqlite3.connect("Photogeniks.db")
c=conn.cursor()
c.execute("SELECT * FROM People")
mysel=c.execute("SELECT * FROM People")
for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i, j, item)
workbook.close()
