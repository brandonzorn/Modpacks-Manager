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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(479, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.items_list = QListWidget(self.frame_4)
        self.items_list.setObjectName(u"items_list")

        self.verticalLayout_5.addWidget(self.items_list)


        self.verticalLayout_4.addWidget(self.frame_4)

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


        self.verticalLayout_4.addWidget(self.frame_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.filters_widget = QWidget(Form)
        self.filters_widget.setObjectName(u"filters_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filters_widget.sizePolicy().hasHeightForWidth())
        self.filters_widget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.filters_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.version_frame = QFrame(self.filters_widget)
        self.version_frame.setObjectName(u"version_frame")
        self.version_frame.setFrameShape(QFrame.StyledPanel)
        self.version_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.version_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.version_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.version_line = QLineEdit(self.version_frame)
        self.version_line.setObjectName(u"version_line")

        self.verticalLayout.addWidget(self.version_line)


        self.verticalLayout_3.addWidget(self.version_frame)

        self.modloader_frame = QFrame(self.filters_widget)
        self.modloader_frame.setObjectName(u"modloader_frame")
        self.modloader_frame.setFrameShape(QFrame.StyledPanel)
        self.modloader_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.modloader_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.modloader_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.modloader_grid = QGridLayout()
        self.modloader_grid.setObjectName(u"modloader_grid")

        self.verticalLayout_2.addLayout(self.modloader_grid)


        self.verticalLayout_3.addWidget(self.modloader_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.filters_widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_btn.setText("")
        self.prev_btn.setText("")
        self.page_lbl.setText(QCoreApplication.translate("Form", u"Page", None))
        self.next_btn.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Version", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Modloader", None))
    # retranslateUi

