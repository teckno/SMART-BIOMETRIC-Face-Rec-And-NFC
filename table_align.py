from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt4.QtGui import QTableView,QApplication
import sys

app = QApplication(sys.argv)

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("Photogeniks.db")
db.open()

projectModel = QSqlQueryModel()
projectModel.setQuery("SELECT * from Student",db)

projectView = QTableView()
projectView.setModel(projectModel)

projectView.show()
app.exec_()
