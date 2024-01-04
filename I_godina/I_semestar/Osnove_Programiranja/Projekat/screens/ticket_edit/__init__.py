from PyQt5 import QtWidgets, QtGui, QtCore
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from utils.generate_seating_plan import generate_seating_plan, locate_seat, generate_seat_tag
from screens.ticket_edit.UI import setupUi
import screens.ticket_edit.local_state as LocalState
from utils.generate_id import generate_string

def TicketEditScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    # frame.setMaximumHeight(900)
    # frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components, functions = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    back_button: QtWidgets.QPushButton = components["back_button"]
    label: QtWidgets.QLabel = components["label"]
    select_widget: QtWidgets.QFrame = components["select_widget"]
    confirm_button: QtWidgets.QPushButton = components["confirm_button"]
    change_showtime_button: QtWidgets.QPushButton = components["change_showtime_button"]
    user_data_gb: QtWidgets.QGroupBox = components["user_data_gb"]
    registered_rb: QtWidgets.QRadioButton = components["registered_rb"]
    unregistered_rb: QtWidgets.QRadioButton = components["unregistered_rb"]
    username_cb: QtWidgets.QComboBox = components["username_cb"]
    name_input: QtWidgets.QLineEdit = components["name_input"]

    setSelectHandler = functions["setSelectHandler"]
    def populate_usernames():
        usernames = [user.username for user in State.db.users.SelectAll()]
        username_cb.addItems(usernames)

    def radio_change():
        username_cb.setEnabled(registered_rb.isChecked())
        name_input.setEnabled(unregistered_rb.isChecked())
        username_cb.clear()
        if registered_rb.isChecked():
            populate_usernames()
    registered_rb.clicked.connect(radio_change)
    unregistered_rb.clicked.connect(radio_change)
    radio_change()

    def selectShowtime(id):
        LocalState.showtime_id = id
        LocalState.showtime = State.db.showtimes.SelectById(id)
        LocalState.seating_plan = generate_seating_plan(id)
        select_widget.hide()
        label.show()
        table.show()
        confirm_button.show()
        change_showtime_button.show()
        user_data_gb.show()
        refresh_table()

    def back_button_click():
        
        parent.back()
    back_button.clicked.connect(back_button_click)
    def cell_click(row, column):
        # print(row, column)
        if LocalState.seating_plan[row][column] == Models.SeatStatus.occupied:
            return MessageBox().warning(frame, "Greška", f"Sedište {generate_seat_tag(row, column)} je zauzeto")
        if LocalState.seating_plan[row][column] == Models.SeatStatus.free:
            LocalState.seating_plan[row][column] = Models.SeatStatus.selected
        else:
            LocalState.seating_plan[row][column] = Models.SeatStatus.free
        refresh_table()
    table.cellClicked.connect(cell_click)
    def refresh_table():
        print("refresh")
        # print(json.dumps(LocalState.seating_plan, indent=4))
        if LocalState.seating_plan is None:
            return
        table.setRowCount(len(LocalState.seating_plan))
        table.setColumnCount(len(LocalState.seating_plan[0]))
        
        # def get_handle_click(film_id):
        #     def handler():
        #         FilmDetailsState.current_film = State.db.films.SelectById(film_id)
        #         parent.show_screen("film_details")
        #     return handler
        brush_free = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush_free.setStyle(QtCore.Qt.SolidPattern)

        brush_occupied = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush_occupied.setStyle(QtCore.Qt.SolidPattern)

        brush_selected = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush_selected.setStyle(QtCore.Qt.SolidPattern)
        for row_index in range(len(LocalState.seating_plan)):
            for column_index in range(len(LocalState.seating_plan[row_index])):
                item = QtWidgets.QTableWidgetItem()
                item.setText(generate_seat_tag(row_index, column_index))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                if LocalState.seating_plan[row_index][column_index] == Models.SeatStatus.free:
                    item.setBackground(brush_free)
                elif LocalState.seating_plan[row_index][column_index] == Models.SeatStatus.occupied:
                    item.setBackground(brush_occupied)
                else:
                    item.setBackground(brush_selected)
                table.setItem(row_index, column_index, item)

    def confirm_button_click():
        tags = []
        for row in range(len(LocalState.seating_plan)):
            for column in range(len(LocalState.seating_plan[0])):
                if LocalState.seating_plan[row][column] == Models.SeatStatus.selected:
                    tags.append(generate_seat_tag(row, column))
        if len(tags) != 1:
            return MessageBox().warning(frame, "Greška", "Morate odabrati jedno sedište da biste izmenili kartu")
        usernames = [user.username for user in State.db.users.SelectAll()]
        username = username_cb.currentText().strip()
        name = name_input.text().strip()
        if registered_rb.isChecked():
            name = None
            if username not in usernames:
                return MessageBox().warning(frame, "Greška", "Morate odabrati validno korisničko ime")
        else:
            username = None
            if name == "":
                return MessageBox().warning(frame, "Greška", "Morate uneti ime i prezime")
        print(username, name)
        LocalState.ticket.showtime_id = LocalState.showtime_id
        LocalState.ticket.seat_tag = tags[0]
        LocalState.ticket.username = username
        LocalState.ticket.full_name = name
        print(LocalState.ticket.toJsonString(2))
        LocalState.showtime_id = None
        LocalState.showtime = None
        LocalState.ticket = None
        select_widget.show()
        label.hide()
        table.hide()
        user_data_gb.hide()
        username_cb.clear()
        name_input.setText("")
        confirm_button.hide()
        change_showtime_button.hide()
        parent.back()
    confirm_button.clicked.connect(confirm_button_click)

    def change_showtime_button_click():
        LocalState.showtime_id = None
        LocalState.showtime = None
        select_widget.show()
        label.hide()
        table.hide()
        user_data_gb.hide()
        username_cb.clear()
        name_input.setText("")
        confirm_button.hide()
        change_showtime_button.hide()
    change_showtime_button.clicked.connect(change_showtime_button_click)

    def populate_data():
        ticket: Models.Ticket = LocalState.ticket
        showtime: Models.Showtime = ticket.showtime.get(State.db)
        LocalState.showtime = showtime
        LocalState.showtime_id = showtime.id
        LocalState.seating_plan = generate_seating_plan(showtime.id)
        row, column = locate_seat(ticket.seat_tag)
        LocalState.seating_plan[row][column] = Models.SeatStatus.selected
        if ticket.full_name is not None:
            name_input.setText(ticket.full_name)
            registered_rb.setChecked(False)
            unregistered_rb.setChecked(True)
        else:
            populate_usernames()
            unregistered_rb.setChecked(False)
            registered_rb.setChecked(True)
            username_cb.setCurrentText(ticket.username)
        refresh_table()

    def showEvent(event):
        refresh_table()
        setSelectHandler(selectShowtime)
        select_widget.hide()
        label.show()
        table.show()
        user_data_gb.show()
        username_cb.clear()
        name_input.setText("")
        confirm_button.show()
        change_showtime_button.show()
        populate_data()
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent

    
    
    return frame

