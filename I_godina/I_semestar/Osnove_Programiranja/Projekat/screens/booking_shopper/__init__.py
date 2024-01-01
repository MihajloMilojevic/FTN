from PyQt5 import QtWidgets, QtGui, QtCore
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from utils.generate_seating_plan import generate_seating_plan
from screens.booking_shopper.UI import setupUi
import screens.booking_shopper.local_state as LocalState
from utils.generate_id import generate_string

def ShopperBookingScreen(parent):
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

    setSelectHandler = functions["setSelectHandler"]

    def selectShowtime(id):
        LocalState.showtime_id = id
        LocalState.showtime = State.db.showtimes.SelectById(id)
        LocalState.seating_plan = generate_seating_plan(id)
        select_widget.hide()
        label.show()
        table.show()
        confirm_button.show()
        change_showtime_button.show()
        refresh_table()
    setSelectHandler(selectShowtime)

    def back_button_click():
        LocalState.showtime_id = None
        LocalState.showtime = None
        select_widget.show()
        label.hide()
        table.hide()
        confirm_button.hide()
        change_showtime_button.hide()
        parent.show_screen(State.user.role)
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
        if len(tags) == 0:
            return MessageBox().warning(frame, "Greška", "Morate odabrati bar jedno sedište da biste rezervisali kartu")
        for tag in tags:
            ticket = Models.Ticket(
                generate_string(10, lower=False, upper=True, digits=False),
                LocalState.showtime_id,
                tag,
                True,
                None,
                State.user.username,
                None,
                None
            )
            State.db.tickets.Insert(ticket)
        LocalState.showtime_id = None
        LocalState.showtime = None
        select_widget.show()
        label.hide()
        table.hide()
        confirm_button.hide()
        change_showtime_button.hide()
        parent.show_screen(State.user.role)
    confirm_button.clicked.connect(confirm_button_click)

    def change_showtime_button_click():
        LocalState.showtime_id = None
        LocalState.showtime = None
        select_widget.show()
        label.hide()
        table.hide()
        confirm_button.hide()
        change_showtime_button.hide()
    change_showtime_button.clicked.connect(change_showtime_button_click)

    


    def showEvent(event):
        refresh_table()
        return QtWidgets.QFrame.showEvent(frame, event)
    frame.showEvent = showEvent

    select_widget.show()
    label.hide()
    table.hide()
    confirm_button.hide()
    change_showtime_button.hide()
    
    return frame

def generate_seat_tag(row, column):
    return f"{row+1}-{chr(ord('A') + column)}"