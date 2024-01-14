from utils.get_desktop import get_desktop
from os import path
from PyQt5 import QtWidgets

def get_save_file_name(frame):
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontUseNativeDialog
    fileName, _ = QtWidgets.QFileDialog.getSaveFileName(frame, 
        "Sačuvaj izveštaj", path.join(get_desktop(), "izvestaj.txt"), "Text Files(*.txt)", options = options)
    return fileName