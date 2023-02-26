# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/home_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_home_page_form(object):
    def setupUi(self, main_home_page_form):
        main_home_page_form.setObjectName("main_home_page_form")
        main_home_page_form.resize(1024, 600)
        self.home_dashboard = QtWidgets.QFrame(main_home_page_form)
        self.home_dashboard.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.home_dashboard.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.home_dashboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_dashboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_dashboard.setObjectName("home_dashboard")
        self.top_bar_home = QtWidgets.QFrame(self.home_dashboard)
        self.top_bar_home.setGeometry(QtCore.QRect(10, 0, 1002, 40))
        self.top_bar_home.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.top_bar_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar_home.setObjectName("top_bar_home")
        self.frame_7 = QtWidgets.QFrame(self.top_bar_home)
        self.frame_7.setGeometry(QtCore.QRect(100, 5, 824, 30))
        self.frame_7.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setGeometry(QtCore.QRect(40, 5, 500, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Rockwell\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.dashboard_main = QtWidgets.QFrame(self.home_dashboard)
        self.dashboard_main.setGeometry(QtCore.QRect(10, 50, 1002, 450))
        self.dashboard_main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dashboard_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboard_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboard_main.setObjectName("dashboard_main")
        self.side_menu_home = QtWidgets.QFrame(self.dashboard_main)
        self.side_menu_home.setGeometry(QtCore.QRect(10, 10, 220, 430))
        self.side_menu_home.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.side_menu_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_home.setObjectName("side_menu_home")
        self.btn_charge_constant_current = QtWidgets.QPushButton(self.side_menu_home)
        self.btn_charge_constant_current.setGeometry(QtCore.QRect(10, 15, 200, 60))
        self.btn_charge_constant_current.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(0, 85, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(85, 170, 255);")
        self.btn_charge_constant_current.setObjectName("btn_charge_constant_current")
        self.btn_charge_constant_voltage = QtWidgets.QPushButton(self.side_menu_home)
        self.btn_charge_constant_voltage.setGeometry(QtCore.QRect(10, 100, 200, 60))
        self.btn_charge_constant_voltage.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(0, 85, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(85, 170, 255);")
        self.btn_charge_constant_voltage.setObjectName("btn_charge_constant_voltage")
        self.btn_charge_reflex = QtWidgets.QPushButton(self.side_menu_home)
        self.btn_charge_reflex.setGeometry(QtCore.QRect(10, 185, 200, 60))
        self.btn_charge_reflex.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(0, 85, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(85, 170, 255);")
        self.btn_charge_reflex.setObjectName("btn_charge_reflex")
        self.btn_discharge = QtWidgets.QPushButton(self.side_menu_home)
        self.btn_discharge.setGeometry(QtCore.QRect(10, 270, 200, 60))
        self.btn_discharge.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(0, 85, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(85, 170, 255);")
        self.btn_discharge.setObjectName("btn_discharge")
        self.btn_wait = QtWidgets.QPushButton(self.side_menu_home)
        self.btn_wait.setGeometry(QtCore.QRect(10, 355, 200, 60))
        self.btn_wait.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(0, 85, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(85, 170, 255);")
        self.btn_wait.setObjectName("btn_wait")
        self.main_workspace = QtWidgets.QFrame(self.dashboard_main)
        self.main_workspace.setGeometry(QtCore.QRect(240, 10, 750, 430))
        self.main_workspace.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_workspace.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_workspace.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_workspace.setObjectName("main_workspace")
        self.buttons_space = QtWidgets.QFrame(self.home_dashboard)
        self.buttons_space.setGeometry(QtCore.QRect(10, 510, 1002, 80))
        self.buttons_space.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buttons_space.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_space.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_space.setObjectName("buttons_space")

        self.retranslateUi(main_home_page_form)
        QtCore.QMetaObject.connectSlotsByName(main_home_page_form)

    def retranslateUi(self, main_home_page_form):
        _translate = QtCore.QCoreApplication.translate
        main_home_page_form.setWindowTitle(_translate("main_home_page_form", "Form"))
        self.label_2.setText(_translate("main_home_page_form", "RF80-M / Home          | Christie Software v1"))
        self.btn_charge_constant_current.setText(_translate("main_home_page_form", "CHARGE CONSTANT CURRENT"))
        self.btn_charge_constant_voltage.setText(_translate("main_home_page_form", "CHARGE CONSTANT VOLTAGE"))
        self.btn_charge_reflex.setText(_translate("main_home_page_form", "CHARGE REFLEX"))
        self.btn_discharge.setText(_translate("main_home_page_form", "DISCHARGE"))
        self.btn_wait.setText(_translate("main_home_page_form", "WAIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_home_page_form = QtWidgets.QWidget()
    ui = Ui_main_home_page_form()
    ui.setupUi(main_home_page_form)
    main_home_page_form.show()
    sys.exit(app.exec_())
