import PySimpleGUI as sg
from quote import *


def empty_response(response, empty_field):
    if response == "":
        sg.theme("dark grey 14")
        layout = [[sg.Text("Enter missing value for ", empty_field, ":")],
                  [sg.InputText(enable_events=True, key="event")]]

        window = sg.Window("Quote Calculator", layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break

            if event == "Next":
                response = values[event]

        window.close()

    return response


class GuiHelp:
    # Theme color
    def __init__(self):
        self.create_theme()

    # Sets layout for first window
    def create_first_window(self, quote):
        # Set the layout for main info page
        layout = [[sg.Text("Choose the type of tank:")],
                  [sg.InputCombo(("Circular", "Rectangular", "Flat Sheet"), size=(40, 1), enable_events=True,
                                 key="tank_type")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("Enter price per square foot:")],
                  [sg.Text("$"), sg.InputText(enable_events=True, key="square_foot_cost")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("Enter weight per square foot:")],
                  [sg.InputText(enable_events=True, key="square_foot_weight"), sg.Text("lbs.")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 1)), sg.Button("Next", size=(6, 1))]]

        # Create setup window
        setup_window = sg.Window("Quote Calculator", layout)

        # Event reader
        exit_a = self.first_window_event_reader(setup_window, quote)

        # Close window
        setup_window.close()

        # Return true if closed, false otherwise
        return exit_a

    @staticmethod
    def create_theme():
        sg.theme("dark grey 14")

    @staticmethod
    # First window event reader
    def first_window_event_reader(setup_window, quote):
        while True:
            event, values = setup_window.read()
            if event == sg.WINDOW_CLOSED:
                return True

            if event == "Next":
                tank = values["tank_type"].lower()
                sq_price = float(values["square_foot_cost"])
                sq_weight = float(values["square_foot_weight"])
                quote.liner = Liner(tank, sq_price, sq_weight)
                return False


