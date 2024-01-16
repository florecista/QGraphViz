import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MainView(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)


app = QApplication([])
mainwindow = MainView()
mainwindow.show()
sys.exit(app.exec_())
# END: bypass license check


if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    app.setOrganizationName("Graph")
    app.setApplicationName("Graph")

    # check license file
    licenseFlag = False

    for licenseFile in glob.glob("*.license"):
        if check_license_file(licenseFile):
            licenseFlag = True
            file = licenseFile

    if licenseFlag:
        mainwindow = MainView()
        mainwindow.license_file = file
        mainwindow.show()
    else:
        print("License is expired or not found.")
        addLicenseWindow = Ui_Registration()
        result = addLicenseWindow.exec_()
        if result == 0:
            sys.exit(0)

        if len(addLicenseWindow.licenseFile) > 0:
            print(
                'License file: "'
                + addLicenseWindow.licenseFile
                + '" is copied to current folder.'
            )

            old_path, base = os.path.split(addLicenseWindow.licenseFile)
            new_path = os.path.join(os.getcwd(), base)
            dest = shutil.copyfile(addLicenseWindow.licenseFile, new_path)

            if check_license_file(dest):
                mainwindow = MainView()
                mainwindow.license_file = base
                mainwindow.show()

    sys.exit(app.exec_())