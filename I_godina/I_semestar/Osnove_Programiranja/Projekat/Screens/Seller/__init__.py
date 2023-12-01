from PyQt5 import QtWidgets
from screens.seller.UI import setupUi
import app.state as State

def SellerScreen(parent):
    frame = QtWidgets.QFrame()
    components = setupUi(frame)
    odjavi_se_button: QtWidgets.QPushButton = components["odjavi_se_button"]
    name_label: QtWidgets.QLabel = components["name_label"]
    user_data_button: QtWidgets.QPushButton = components["user_data_button"]
    
    def odjavi_se_button_click():
        State.user = None
        parent.show_screen("unregistered")
    odjavi_se_button.clicked.connect(odjavi_se_button_click)

    def user_data_button_click():
        parent.show_screen("user_data")
    user_data_button.clicked.connect(user_data_button_click)
    
    def showEvent(event):
        name_label.setText(f"Zdravo, {State.user.name} {State.user.surname}")
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent
    return frame