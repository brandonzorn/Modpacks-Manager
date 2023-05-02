import sys
import time

from PySide6.QtCore import Qt

import nlight_res_rc
import darkdetect
from PySide6.QtWidgets import QApplication

from modrinthmanager.utils.utils import get_ui_style, Worker
from modrinthmanager.windows.MainWindow import MainWindow


def update_theme():
    def set_style():
        app.setStyleSheet(get_ui_style(darkdetect.theme()))
        update_theme()

    def theme_updater():
        theme = darkdetect.theme()
        while True:
            time.sleep(1)
            if darkdetect.theme() != theme or app.applicationState() == app.applicationState().ApplicationInactive:
                return

    Worker(target=theme_updater, callback=set_style).start()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    QApplication.setStyle('Fusion')
    app = QApplication(sys.argv)
    app.setStyleSheet(get_ui_style(darkdetect.theme()))
    update_theme()
    window = MainWindow()
    sys.exit(app.exec())
