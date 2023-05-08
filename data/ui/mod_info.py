# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_info.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(557, 413)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.add_btn = QPushButton(self.frame_3)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.add_btn)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.icon_lbl = QLabel(self.frame_2)
        self.icon_lbl.setObjectName(u"icon_lbl")

        self.verticalLayout_2.addWidget(self.icon_lbl)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_lbl = QLabel(self.frame)
        self.name_lbl.setObjectName(u"name_lbl")

        self.verticalLayout.addWidget(self.name_lbl)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.description_text = QTextBrowser(Dialog)
        self.description_text.setObjectName(u"description_text")

        self.verticalLayout_3.addWidget(self.description_text)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.items_list = QListWidget(Dialog)
        self.items_list.setObjectName(u"items_list")

        self.horizontalLayout_2.addWidget(self.items_list)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.add_btn.setText("")
        self.icon_lbl.setText(QCoreApplication.translate("Dialog", u"icon", None))
        self.name_lbl.setText(QCoreApplication.translate("Dialog", u"name", None))
    # retranslateUi

