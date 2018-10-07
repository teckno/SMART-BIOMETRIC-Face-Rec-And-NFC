import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('output4.xlsx')
worksheet = workbook.add_worksheet()

conn=sqlite3.connect("Photogeniks.db")
c=conn.cursor()
c.execute("SELECT * FROM People")
mysel=c.execute("SELECT * FROM People")
for i, row in enumerate(mysel):
    print row
    worksheet.write(i, 0, row[0])
    worksheet.write(i, 1, row[1])
workbook.close()
