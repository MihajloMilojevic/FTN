from PyQt5 import QtWidgets
from screens.reports.UI import setupUi

def ReportsScreen(parent):
    frame = QtWidgets.QFrame()

    components = setupUi(frame)
    back_button: QtWidgets.QPushButton = components["back_button"]
    report_a_button:  QtWidgets.QPushButton = components["report_a_button"]
    report_b_button:  QtWidgets.QPushButton = components["report_b_button"]
    report_c_button:  QtWidgets.QPushButton = components["report_c_button"]
    report_d_button:  QtWidgets.QPushButton = components["report_d_button"]
    report_e_button:  QtWidgets.QPushButton = components["report_e_button"]
    report_f_button:  QtWidgets.QPushButton = components["report_f_button"]
    report_g_button:  QtWidgets.QPushButton = components["report_g_button"]
    report_h_button:  QtWidgets.QPushButton = components["report_h_button"]

    def report_a_button_click():
        parent.show_screen("report_a")
    report_a_button.clicked.connect(report_a_button_click)
    def report_b_button_click():
        parent.show_screen("report_b")
    report_b_button.clicked.connect(report_b_button_click)
    def report_c_button_click():
        parent.show_screen("report_c")
    report_c_button.clicked.connect(report_c_button_click)
    def report_d_button_click():
        parent.show_screen("report_d")
    report_d_button.clicked.connect(report_d_button_click)
    def report_e_button_click():
        parent.show_screen("report_e")
    report_e_button.clicked.connect(report_e_button_click)
    def report_f_button_click():
        parent.show_screen("report_f")
    report_f_button.clicked.connect(report_f_button_click)
    def report_g_button_click():
        parent.show_screen("report_g")
    report_g_button.clicked.connect(report_g_button_click)
    def report_h_button_click():
        parent.show_screen("report_h")
    report_h_button.clicked.connect(report_h_button_click)

    def back_button_click():
        parent.back()
    back_button.clicked.connect(back_button_click)

    return frame