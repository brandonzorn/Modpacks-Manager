# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_search.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.items_list = QListWidget(Form)
        self.items_list.setObjectName(u"items_list")

        self.verticalLayout.addWidget(self.items_list)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.search_line = QLineEdit(self.widget)
        self.search_line.setObjectName(u"search_line")

        self.horizontalLayout_2.addWidget(self.search_line)

        self.search_btn = QPushButton(self.widget)
        self.search_btn.setObjectName(u"search_btn")

        self.horizontalLayout_2.addWidget(self.search_btn)


        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.prev_btn = QPushButton(self.widget_2)
        self.prev_btn.setObjectName(u"prev_btn")

        self.horizontalLayout_4.addWidget(self.prev_btn)

        self.page_lbl = QLabel(self.widget_2)
        self.page_lbl.setObjectName(u"page_lbl")

        self.horizontalLayout_4.addWidget(self.page_lbl)

        self.next_btn = QPushButton(self.widget_2)
        self.next_btn.setObjectName(u"next_btn")

        self.horizontalLayout_4.addWidget(self.next_btn)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.prev_btn.setText(QCoreApplication.translate("Form", u"<", None))
        self.page_lbl.setText(QCoreApplication.translate("Form", u"Page", None))
        self.next_btn.setText(QCoreApplication.translate("Form", u">", None))
    # retranslateUi

