# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/all_views.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_all_views_form(object):
    def setupUi(self, all_views_form):
        all_views_form.setObjectName("all_views_form")
        all_views_form.resize(528, 343)
        self.win_all_views = QtWidgets.QFrame(all_views_form)
        self.win_all_views.setGeometry(QtCore.QRect(0, 0, 530, 350))
        self.win_all_views.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.win_all_views.setFrameShadow(QtWidgets.QFrame.Raised)
        self.win_all_views.setObjectName("win_all_views")

        self.retranslateUi(all_views_form)
        QtCore.QMetaObject.connectSlotsByName(all_views_form)

    def retranslateUi(self, all_views_form):
        _translate = QtCore.QCoreApplication.translate
        all_views_form.setWindowTitle(_translate("all_views_form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    all_views_form = QtWidgets.QWidget()
    ui = Ui_all_views_form()
    ui.setupUi(all_views_form)
    all_views_form.show()
    sys.exit(app.exec_())
