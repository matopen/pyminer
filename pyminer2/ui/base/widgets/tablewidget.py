import sys

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication
from PyQt5.QtCore import QCoreApplication


class PMTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("")
        self.setAlternatingRowColors(False)
        self.setObjectName("tableWidget_dataset")
        self.setColumnCount(30)
        self.setRowCount(30)

    def setup_ui(self):
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(7, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(8, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(9, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(10, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(11, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(12, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(13, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(14, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(15, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(16, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(17, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(18, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(19, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(20, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(21, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(22, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(23, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(24, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(25, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(26, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(27, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(28, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(29, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(7, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(8, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(9, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(10, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(11, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(12, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(13, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(14, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(15, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(16, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(17, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(18, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(19, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(20, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(21, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(22, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(23, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(24, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(25, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(26, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(27, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(28, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(29, item)

        self.translate()

    def translate(self):
        _translate = QCoreApplication.translate
        item = self.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "19"))
        item = self.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "20"))
        item = self.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "21"))
        item = self.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "22"))
        item = self.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "23"))
        item = self.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "24"))
        item = self.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "25"))
        item = self.verticalHeaderItem(25)
        item.setText(_translate("MainWindow", "26"))
        item = self.verticalHeaderItem(26)
        item.setText(_translate("MainWindow", "27"))
        item = self.verticalHeaderItem(27)
        item.setText(_translate("MainWindow", "28"))
        item = self.verticalHeaderItem(28)
        item.setText(_translate("MainWindow", "29"))
        item = self.verticalHeaderItem(29)
        item.setText(_translate("MainWindow", "30"))
        item = self.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "C1"))
        item = self.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "C2"))
        item = self.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C3"))
        item = self.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "C4"))
        item = self.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "C5"))
        item = self.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "C6"))
        item = self.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "C7"))
        item = self.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "C8"))
        item = self.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "C9"))
        item = self.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "C10"))
        item = self.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "C11"))
        item = self.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "C12"))
        item = self.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "C13"))
        item = self.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "C14"))
        item = self.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "C15"))
        item = self.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "C16"))
        item = self.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "C17"))
        item = self.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "C18"))
        item = self.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "C19"))
        item = self.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "C20"))
        item = self.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "C21"))
        item = self.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "C22"))
        item = self.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "C23"))
        item = self.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "C24"))
        item = self.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "C25"))
        item = self.horizontalHeaderItem(25)
        item.setText(_translate("MainWindow", "C26"))
        item = self.horizontalHeaderItem(26)
        item.setText(_translate("MainWindow", "C27"))
        item = self.horizontalHeaderItem(27)
        item.setText(_translate("MainWindow", "C28"))
        item = self.horizontalHeaderItem(28)
        item.setText(_translate("MainWindow", "C29"))
        item = self.horizontalHeaderItem(29)
        item.setText(_translate("MainWindow", "C30"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    graphics = PMTableWidget()
    graphics.show()

    sys.exit(app.exec_())