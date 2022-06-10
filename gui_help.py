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

    @staticmethod
    def create_theme():
        sg.theme("dark grey 14")

    # Creates first window (liner setup)
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

    # Creates second window (liner customizations)
    def create_second_window(self, quote):
        # Circular configuration
        if isinstance(quote.liner.info, CLiner):
            exit_b = self.create_circular_configuration_window(quote)
        elif isinstance(quote.liner.info, RLiner):
            exit_b = self.create_rectangular_configuration_window(quote)
        elif isinstance(quote.liner.info, FLiner):
            exit_b = self.create_flat_sheet_configuration_window(quote)
        else:
            exit_b = False
        return exit_b

    # Creates circular configuration window
    def create_circular_configuration_window(self, quote):
        # Get circular tank input from user
        layout = [[sg.Text("Enter diameter of tank:")],
                  [sg.InputText(enable_events=True, size=(5, 2), key="tank_dm_ft"), sg.Text("ft."),
                   sg.InputText(enable_events=True, size=(3, 2), key="tank_dm_in"), sg.Text("in.")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("Enter depth of tank:")],
                  [sg.InputText(enable_events=True, size=(5, 2), key="tank_dp_ft"), sg.Text("ft."),
                   sg.InputText(enable_events=True, size=(3, 2), key="tank_dp_in"), sg.Text("in.")],
                  [sg.Text("Please enter any extensions to depth:"),
                   sg.InputText(enable_events=True, size=(3, 2), key="tank_dp_ex_in"), sg.Text("in.")],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(6, 1)), sg.Text(size=(34, 2)), sg.Button("Next", size=(6, 1))]]

        # Create setup window
        window = sg.Window("Quote Calculator", layout)

        # Event reader
        exit_b = self.circular_config_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false otherwise
        return exit_b

    @staticmethod
    # Circular configuration event reader
    def circular_config_event_reader(window, quote):
        # Capture values after next button is pushed
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                return True

            if event == "Next":
                diameter_ft = float(values["tank_dm_ft"])
                diameter_inch = float(values["tank_dm_in"])
                depth_ft = float(values["tank_dp_ft"])
                depth_inch = float(values["tank_dm_in"])
                depth_extensions = float(values["tank_dp_ex_in"])
                quote.liner.info.configure(diameter_ft, diameter_inch, depth_ft, depth_inch, depth_extensions)
                return False

            if event == "Back":
                return True

    # Creates rectangular configuration window
    def create_rectangular_configuration_window(self, quote):
        pass

    # Creates flat sheet configuration window
    def create_flat_sheet_configuration_window(self, quote):
        pass
