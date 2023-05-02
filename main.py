import sys


from PySide6.QtWidgets import QApplication

from modrinthmanager.widgets.mod_search import ModSearch


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModSearch()
    window.show()
    sys.exit(app.exec())
