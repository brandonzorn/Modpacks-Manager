# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modpacks.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(578, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.items_list = QListWidget(self.frame_4)
        self.items_list.setObjectName(u"items_list")

        self.verticalLayout_5.addWidget(self.items_list)


        self.horizontalLayout.addWidget(self.frame_4)

        self.filters_widget = QWidget(Form)
        self.filters_widget.setObjectName(u"filters_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filters_widget.sizePolicy().hasHeightForWidth())
        self.filters_widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.filters_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.filters_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.version_line = QLineEdit(self.frame_2)
        self.version_line.setObjectName(u"version_line")

        self.verticalLayout_2.addWidget(self.version_line)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.filters_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.modloader_line = QLineEdit(self.frame_3)
        self.modloader_line.setObjectName(u"modloader_line")

        self.verticalLayout_4.addWidget(self.modloader_line)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.download = QPushButton(self.filters_widget)
        self.download.setObjectName(u"download")

        self.verticalLayout_3.addWidget(self.download)

        self.cur_mod = QLabel(self.filters_widget)
        self.cur_mod.setObjectName(u"cur_mod")
        self.cur_mod.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.cur_mod)

        self.download_progress = QProgressBar(self.filters_widget)
        self.download_progress.setObjectName(u"download_progress")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.download_progress.sizePolicy().hasHeightForWidth())
        self.download_progress.setSizePolicy(sizePolicy2)
        self.download_progress.setMaximum(0)
        self.download_progress.setValue(0)

        self.verticalLayout_3.addWidget(self.download_progress)


        self.horizontalLayout.addWidget(self.filters_widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Version", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Modloader", None))
        self.download.setText(QCoreApplication.translate("Form", u"Download", None))
        self.cur_mod.setText("")
        self.download_progress.setFormat(QCoreApplication.translate("Form", u"%v/%m", None))
    # retranslateUi

