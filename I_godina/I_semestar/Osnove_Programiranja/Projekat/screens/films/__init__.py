from PyQt5 import QtWidgets, QtGui, QtCore
import app.state as State
import database.models as Models
from utils.message_box import MessageBox
from screens.films.UI import setupUi
import screens.films.local_state as LocalState
import screens.film_details.local_state as FilmDetailsState

def FilmsScreen(parent):
    frame = QtWidgets.QFrame()
    frame.setMinimumSize(400, 150)
    # frame.setMaximumHeight(900)
    # frame.setMaximumWidth(500)
    # frame.setStyleSheet("border: 1px solid red")
    components, functions = setupUi(frame)
    table: QtWidgets.QTableWidget = components["table"]
    name_input: QtWidgets.QLineEdit = components["name_input"]
    # search_button: QtWidgets.QPushButton = components["search_button"]
    filters_button: QtWidgets.QPushButton = components["filters_button"]
    back_button: QtWidgets.QPushButton = components["back_button"]
    min_duration_sb: QtWidgets.QSpinBox = components["min_duration_sb"]
    max_duration_sb: QtWidgets.QSpinBox = components["max_duration_sb"]
    filters_scroll_area: QtWidgets.QScrollArea = components["filters_scroll_area"]

    add_genre = functions["add_genre"]
    add_role = functions["add_role"]
    add_director = functions["add_director"]
    add_country = functions["add_country"]
    add_year = functions["add_year"]

    def back_button_click():
        name_input.setText("")
        parent.back()
    back_button.clicked.connect(back_button_click)
    def refresh_table():
        print("refresh")
        table.setRowCount(0)
        data = LocalState.get_film_list()
        table.setRowCount(len(data))
        def get_handle_click(film_id):
            def handler():
                FilmDetailsState.current_film = State.db.films.SelectById(film_id)
                parent.show_screen("film_details")
            return handler
        for index in range(len(data)):
            film: Models.Film  = data[index]
            widget = QtWidgets.QWidget()
            widget.setLayout(QtWidgets.QVBoxLayout())
            details_button = QtWidgets.QPushButton("Detalji")
            details_button.setStyleSheet("border: 1px solid black; padding: 5px 10px")
            details_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            details_button.clicked.connect(get_handle_click(film.id))
            widget.layout().addWidget(details_button)
            widget.layout().setContentsMargins(5, 5, 5, 5)
            table.setCellWidget(index, 0, widget)
            item = QtWidgets.QTableWidgetItem(film.id)
            table.setItem(index, 1, item)
            item = QtWidgets.QTableWidgetItem(film.name)
            table.setItem(index, 2, item)
            item = QtWidgets.QTableWidgetItem(", ".join(film.genres))
            table.setItem(index, 3, item)
            item = QtWidgets.QTableWidgetItem(str(film.duration))
            table.setItem(index, 4, item)
            item = QtWidgets.QTableWidgetItem(film.director)
            table.setItem(index, 5, item)
            item = QtWidgets.QTableWidgetItem(", ".join(film.main_roles))
            table.setItem(index, 6, item)
            item = QtWidgets.QTableWidgetItem(film.country)
            table.setItem(index, 7, item)
            item = QtWidgets.QTableWidgetItem(str(film.year))
            table.setItem(index, 8, item)
        table.resizeRowsToContents()
    # search_button.clicked.connect(refresh_table)
    def filters_button_click():
        if filters_scroll_area.isVisible():
            filters_scroll_area.hide()
        else:
            filters_scroll_area.show()
    filters_button.clicked.connect(filters_button_click)
    def name_input_change():
        LocalState.criteria["name"] = name_input.text()
        print(f"Name set to {LocalState.criteria['name']}")
        refresh_table()
    name_input.textChanged.connect(name_input_change)

    def populate_genres():
        def get_check_box_change(box: QtWidgets.QCheckBox):
            def ret_func():
                if box.isChecked():
                    LocalState.criteria["genre"].append(box.text())
                else:
                    LocalState.criteria["genre"].remove(box.text())
                refresh_table()
            return ret_func
        for genre in Models.Genres.all_genres:
            check_box = add_genre(genre)
            check_box.stateChanged.connect(get_check_box_change(check_box))

    def setup_duration():
        all_durations = [film.duration for film in State.db.films.SelectAll()]
        min_duration = min(all_durations)
        max_duration = max(all_durations)
        min_duration_sb.setMinimum(min_duration)
        max_duration_sb.setMinimum(min_duration)
        min_duration_sb.setMaximum(max_duration)
        max_duration_sb.setMaximum(max_duration)
        min_duration_sb.setValue(min_duration)
        max_duration_sb.setValue(max_duration)
        LocalState.criteria["duration"]["min"] = min_duration
        LocalState.criteria["duration"]["max"] = max_duration

        def min_change():
            LocalState.criteria["duration"]["min"] = min_duration_sb.value()
            refresh_table()
        def max_change():
            LocalState.criteria["duration"]["max"] = max_duration_sb.value()
            refresh_table()
        min_duration_sb.valueChanged.connect(min_change)
        max_duration_sb.valueChanged.connect(max_change)

    def populate_roles():
        def get_check_box_change(box: QtWidgets.QCheckBox):
            def ret_func():
                if box.isChecked():
                    LocalState.criteria["role"].append(box.text())
                else:
                    LocalState.criteria["role"].remove(box.text())
                refresh_table()
            return ret_func
        data = set()
        for film in State.db.films.SelectAll():
            data.update(set(film.main_roles))
        for text in data:
            check_box = add_role(text)
            check_box.stateChanged.connect(get_check_box_change(check_box))

    def populate_directors():
        def get_check_box_change(box: QtWidgets.QCheckBox):
            def ret_func():
                if box.isChecked():
                    LocalState.criteria["director"].append(box.text())
                else:
                    LocalState.criteria["director"].remove(box.text())
                refresh_table()
            return ret_func
        data = set()
        for film in State.db.films.SelectAll():
            data.add(film.director)
        for text in data:
            check_box = add_director(text)
            check_box.stateChanged.connect(get_check_box_change(check_box))

    def populate_countries():
        def get_check_box_change(box: QtWidgets.QCheckBox):
            def ret_func():
                if box.isChecked():
                    LocalState.criteria["country"].append(box.text())
                else:
                    LocalState.criteria["country"].remove(box.text())
                refresh_table()
            return ret_func
        data = set()
        for film in State.db.films.SelectAll():
            data.add(film.country)
        for text in data:
            check_box = add_country(text)
            check_box.stateChanged.connect(get_check_box_change(check_box))

    def populate_years():
        def get_check_box_change(box: QtWidgets.QCheckBox):
            def ret_func():
                if box.isChecked():
                    LocalState.criteria["year"].append(int(box.text()))
                else:
                    LocalState.criteria["year"].remove(int(box.text()))
                refresh_table()
            return ret_func
        data = set()
        for film in State.db.films.SelectAll():
            data.add(film.year)
        ordered_data = reversed(sorted(list(data)))
        
        for year in ordered_data:
            check_box = add_year(str(year))
            check_box.stateChanged.connect(get_check_box_change(check_box))


    def showEvent(event):
        refresh_table()
        return QtWidgets.QFrame.showEvent(frame, event)
    
    
    filters_scroll_area.hide()
    
    populate_genres()
    setup_duration()
    populate_roles()
    populate_directors()
    populate_countries()
    populate_years()
    

    frame.showEvent = showEvent
    return frame
