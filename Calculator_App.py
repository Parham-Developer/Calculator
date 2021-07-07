# Parham
# 7 hour project
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 583)
        MainWindow.setMinimumSize(QtCore.QSize(311, 583))
        MainWindow.setMaximumSize(QtCore.QSize(311, 583))
        MainWindow.setStyleSheet("background-color: #17181a;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.upper_re_l = QtWidgets.QLabel(self.centralwidget)
        self.upper_re_l.setGeometry(QtCore.QRect(20, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.upper_re_l.setFont(font)
        self.upper_re_l.setStyleSheet("color: #88888a")
        self.upper_re_l.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.upper_re_l.setObjectName("upper_re_l")
        self.res_l = QtWidgets.QLabel(self.centralwidget)
        self.res_l.setGeometry(QtCore.QRect(20, 60, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        self.res_l.setFont(font)
        self.res_l.setStyleSheet("color: #ffffff;")
        self.res_l.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.res_l.setObjectName("res_l")
        self.kla_op = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.open_cl())
        self.kla_op.setGeometry(QtCore.QRect(90, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.kla_op.setFont(font)
        self.kla_op.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self.kla_op.setObjectName("kla_op")
        self.clam_cl = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.close_cl())
        self.clam_cl.setGeometry(QtCore.QRect(160, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.clam_cl.setFont(font)
        self.clam_cl.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self.clam_cl.setObjectName("clam_cl")
        self.divide = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.op("÷"))
        self.divide.setGeometry(QtCore.QRect(230, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.divide.setFont(font)
        self.divide.setStyleSheet("background-color: #ff9500;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #ffffff;")
        self.divide.setObjectName("divide")
        self.x = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.op("x"))
        self.x.setGeometry(QtCore.QRect(230, 300, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.x.setFont(font)
        self.x.setStyleSheet("background-color: #ff9500;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #ffffff;")
        self.x.setObjectName("x")
        self.minus = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.op("-"))
        self.minus.setGeometry(QtCore.QRect(230, 370, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.minus.setFont(font)
        self.minus.setStyleSheet("background-color: #ff9500;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #ffffff;")
        self.minus.setObjectName("minus")
        self.plus = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.op("+"))
        self.plus.setGeometry(QtCore.QRect(230, 440, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.plus.setFont(font)
        self.plus.setStyleSheet("background-color: #ff9500;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #ffffff;")
        self.plus.setObjectName("plus")
        self.equal = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.equal_())
        self.equal.setGeometry(QtCore.QRect(230, 510, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.equal.setFont(font)
        self.equal.setStyleSheet("background-color: #2ec973;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #ffffff;")
        self.equal.setObjectName("equal")
        self.c_b = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.cls())
        self.c_b.setGeometry(QtCore.QRect(20, 160, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.c_b.setFont(font)
        self.c_b.setStyleSheet("background-color: #2d191e;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f4434d;")
        self.c_b.setObjectName("c_b")
        self._9 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(9))
        self._9.setGeometry(QtCore.QRect(160, 300, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._9.setFont(font)
        self._9.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._9.setObjectName("_9")
        self._8 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(8))
        self._8.setGeometry(QtCore.QRect(90, 300, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._8.setFont(font)
        self._8.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._8.setObjectName("_8")
        self._7 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(7))
        self._7.setGeometry(QtCore.QRect(20, 300, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._7.setFont(font)
        self._7.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._7.setObjectName("_7")
        self._6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(6))
        self._6.setGeometry(QtCore.QRect(160, 370, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._6.setFont(font)
        self._6.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._6.setObjectName("_6")
        self._5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(5))
        self._5.setGeometry(QtCore.QRect(90, 370, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._5.setFont(font)
        self._5.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._5.setObjectName("_5")
        self._4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(4))
        self._4.setGeometry(QtCore.QRect(20, 370, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._4.setFont(font)
        self._4.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._4.setObjectName("_4")
        self._3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(3))
        self._3.setGeometry(QtCore.QRect(160, 440, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._3.setFont(font)
        self._3.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._3.setObjectName("_3")
        self._2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(2))
        self._2.setGeometry(QtCore.QRect(90, 440, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._2.setFont(font)
        self._2.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._2.setObjectName("_2")
        self._1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(1))
        self._1.setGeometry(QtCore.QRect(20, 440, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._1.setFont(font)
        self._1.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._1.setObjectName("_1")
        self.dot = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dotter())
        self.dot.setGeometry(QtCore.QRect(160, 510, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.dot.setFont(font)
        self.dot.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self.dot.setObjectName("dot")
        self._0 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_num(0))
        self._0.setGeometry(QtCore.QRect(20, 510, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self._0.setFont(font)
        self._0.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self._0.setObjectName("_0")
        self.min_p_b = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.min_pl())
        self.min_p_b.setGeometry(QtCore.QRect(20, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.min_p_b.setFont(font)
        self.min_p_b.setStyleSheet("background-color: #222427;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f1f2f2;")
        self.min_p_b.setObjectName("min_p_b")
        self.back_b = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.back_space())
        self.back_b.setGeometry(QtCore.QRect(130, 160, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.back_b.setFont(font)
        self.back_b.setStyleSheet("background-color: #2d191e;\n"
        "border: False;\n"
        "border-radius: 22px;\n"
        "color: #f4434d;")
        self.back_b.setObjectName("back_b")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_num(self, num):
        if self.res_l.text() == "0":
            self.res_l.setText(str(num))

        elif self.res_l.text() != "0":
            try:
                number = f"{self.res_l.text()}{str(num)}"
                self.num_checker(number, "res")
            except IndexError:
                pass

    def num_checker(self, x, m):
        if m == "up":
            if len(str(x)) <= 35:
                self.upper_re_l.setText(str(x))
            else:
                raise IndexError

        elif m == "res":
            if len(str(x)) <= 20:
                self.res_l.setText(str(x))
            else:
                raise IndexError

    def back_space(self):
        screen = self.res_l.text()
        screen = screen[:-1]
        if screen == "":
            self.res_l.setText("0")
        elif screen == "-":
            self.res_l.setText("0")
        else:
            self.res_l.setText(str(screen))

    def min_pl(self):
        if "-" in self.res_l.text():
            if "(" in self.res_l.text():
                x = self.res_l.text()
                x = x.split("-")

                self.res_l.setText(f"{x[0]}{x[1]}")
            else:
                x = self.res_l.text().split("-")
                x = x[1]
                self.res_l.setText(str(x))
        elif self.res_l.text() == "0":
            pass
        else:
            if "(" in self.res_l.text():
                self.res_l.setText(f"{self.res_l.text()}-")
            else:
                self.res_l.setText(f"-{self.res_l.text()}")

    def dotter(self):
        if "." in self.res_l.text():
            pass
        else:
            num = self.res_l.text()
            l_num = num[-1]
            try:
                x = int(l_num)
                self.res_l.setText(f"{num}.")
            except ValueError:
                if l_num == "(":
                    pass
                elif l_num == ")":
                    pass

    def cls(self):
        self.res_l.setText("0")
        self.upper_re_l.setText("")

    def op(self, ope):
        try:
            num = self.res_l.text()
            if num[-1] == ".":
                num = num[:-1]
            scr = self.upper_re_l.text()
            self.num_checker(f'{scr}{num}{ope}', "up")
            self.res_l.setText("0")
        except IndexError:
            pass

    def equal_(self):
        try:
            sc = self.res_l.text()
            scr = self.upper_re_l.text()
            scru = f'{scr}{sc}'
            if scru[-1] == ".":
                scru = scru[:-1]
            if scru[-2] == "+":
                if scru[-1] == "0":
                    scru = scru[:-2]
            elif scru[-2] == "-":
                if scru[-1] == "0":
                    scru = scru[:-2]
            elif scru[-2] == "x":
                if scru[-1] == "0":
                    scru = scru[:-2]
            elif scru[-2] == "÷":
                if scru[-1] == "0":
                    scru = scru[:-2]
            if "x" in scru:
                scru = scru.replace("x", "*")
            if "÷" in scru:
                scru = scru.replace("÷", "/")
            try:
                x = eval(scru)
                x = self.divider(x)
            except SyntaxError:
                self.res_l.setText("ERROR")
                self.upper_re_l.setText("ERROR")
            try:
                if "*" in scru:
                    scru = scru.replace("*", "x")
                if "/" in scru:
                    scru = scru.replace("/", "÷")
                self.num_checker(scru, "up")
                self.num_checker(str(x), "res")
            except:
                self.res_l.setText("ERROR")
                self.upper_re_l.setText("ERROR")
        except:
            pass

    def divider(self, x):
        x = str(x)
        if x[-1] == "0":
            x = x.split(".")
            x = x[0]
            x = str(x)
            return x
        else:
            return x

    def open_cl(self):
        scr = self.res_l.text()
        l_scr = scr[-1]
        try:
            l = int(l_scr)
            if scr == "0":
                self.res_l.setText("(")
            else:
                self.op("x")
                self.res_l.setText("(")
        except ValueError:
            if l_scr == ".":
                self.op("x")
                self.res_l.setText("(")
            if l_scr == ")":
                self.op("x")
                self.res_l.setText("(")
            else:
                n_scr = f'{scr}('
                self.res_l.setText(n_scr)

    def close_cl(self):
        scr = self.res_l.text()
        l_scr = scr[-1]
        if scr == "0":
            pass
        elif l_scr == ".":
            n_scr = f'{scr}0)'
            self.res_l.setText(n_scr)
        else:
            n_scr = f'{scr})'
            self.res_l.setText(n_scr)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.upper_re_l.setText(_translate("MainWindow", ""))
        self.res_l.setText(_translate("MainWindow", "0"))
        self.kla_op.setText(_translate("MainWindow", "("))
        self.clam_cl.setText(_translate("MainWindow", ")"))
        self.divide.setText(_translate("MainWindow", "÷"))
        self.x.setText(_translate("MainWindow", "x"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.equal.setText(_translate("MainWindow", "="))
        self.c_b.setText(_translate("MainWindow", "C"))
        self._9.setText(_translate("MainWindow", "9"))
        self._8.setText(_translate("MainWindow", "8"))
        self._7.setText(_translate("MainWindow", "7"))
        self._6.setText(_translate("MainWindow", "6"))
        self._5.setText(_translate("MainWindow", "5"))
        self._4.setText(_translate("MainWindow", "4"))
        self._3.setText(_translate("MainWindow", "3"))
        self._2.setText(_translate("MainWindow", "2"))
        self._1.setText(_translate("MainWindow", "1"))
        self.dot.setText(_translate("MainWindow", "."))
        self._0.setText(_translate("MainWindow", "0"))
        self.min_p_b.setText(_translate("MainWindow", "+/-"))
        self.back_b.setText(_translate("MainWindow", "<-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
