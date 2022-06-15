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
        self.customization = None
        self.exit = False

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
                  [sg.Text("$"), sg.InputText(enable_events=True, key="square_foot_cost", size=(10, 1))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("Enter weight per square foot:")],
                  [sg.InputText(enable_events=True, key="square_foot_weight", size=(8, 1)), sg.Text("lbs.")],
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

    # First window event reader
    def first_window_event_reader(self, setup_window, quote):
        while True:
            event, values = setup_window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Next":
                tank = values["tank_type"].lower()
                sq_price = float(values["square_foot_cost"])
                sq_weight = float(values["square_foot_weight"])
                quote.lining_system.liner = Liner(tank, sq_price, sq_weight)
                return False

    # Creates second window (liner customizations)
    def create_second_window(self, quote):
        # Circular configuration
        if isinstance(quote.lining_system.liner.info, CLiner):
            exit_b = self.create_circular_configuration_window(quote)
        elif isinstance(quote.lining_system.liner.info, RLiner):
            exit_b = self.create_rectangular_configuration_window(quote)
        elif isinstance(quote.lining_system.liner.info, FLiner):
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

        # Create window
        window = sg.Window("Quote Calculator", layout)

        # Event reader
        exit_b = self.circular_config_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false otherwise
        return exit_b

    # Circular configuration event reader
    def circular_config_event_reader(self, window, quote):
        # Capture values after next button is pushed
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Next":
                diameter_ft = float(values["tank_dm_ft"])
                diameter_inch = float(values["tank_dm_in"])
                depth_ft = float(values["tank_dp_ft"])
                depth_inch = float(values["tank_dm_in"])
                depth_extensions = float(values["tank_dp_ex_in"])
                quote.lining_system.liner.info.configure(diameter_ft, diameter_inch, depth_ft,
                                                         depth_inch, depth_extensions)
                return False
            if event == "Back":
                return True

    # Creates rectangular configuration window
    def create_rectangular_configuration_window(self, quote):
        # Get rectangular tank input from user
        layout = [[sg.Text("Enter length of tank:")],
                  [sg.InputText(enable_events=True, size=(5, 2), key="tank_lgth_ft"), sg.Text("ft."),
                   sg.InputText(enable_events=True, size=(3, 2), key="tank_lgth_in"), sg.Text("in.")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("Enter width of tank:")],
                  [sg.InputText(enable_events=True, size=(5, 2), key="tank_wdth_ft"), sg.Text("ft."),
                   sg.InputText(enable_events=True, size=(3, 2), key="tank_wdth_in"), sg.Text("in.")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("Enter depth of tank:")],
                  [sg.InputText(enable_events=True, size=(5, 2), key="tank_dp_ft"), sg.Text("ft."),
                   sg.InputText(enable_events=True, size=(3, 2), key="tank_dp_in"), sg.Text("in.")],
                  [sg.Text("Please enter any extensions to depth:"),
                   sg.InputText(enable_events=True, size=(3, 2), key="tank_dp_ex_in"), sg.Text("in.")],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(6, 1)), sg.Text(size=(34, 2)), sg.Button("Next", size=(6, 1))]]

        # Create window
        window = sg.Window("Quote Calculator", layout)

        # Event reader
        exit_b = self.rectangular_config_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false otherwise
        return exit_b

    # Rectangular configuration event reader
    def rectangular_config_event_reader(self, window, quote):
        # Capture values after next button is pushed
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Next":
                length_ft = float(values["tank_lgth_ft"])
                length_inch = float(values["tank_lgth_in"])
                width_ft = float(values["tank_wdth_ft"])
                width_inch = float(values["tank_wdth_in"])
                depth_ft = float(values["tank_dp_ft"])
                depth_inch = float(values["tank_dp_in"])
                depth_extensions = float(values["tank_dp_ex_in"])
                quote.lining_system.liner.info.configure(length_ft, length_inch, width_ft, width_inch, depth_ft
                                           , depth_inch, depth_extensions)
                return False
            if event == "Back":
                return True

    # Creates flat sheet configuration window
    def create_flat_sheet_configuration_window(self, quote):
        # Get flat sheet input from user
        layout = [[sg.Text("Enter length of liner:")],
                  [sg.InputText(enable_events=True, size=(5, 2), key="tank_lgth_ft"), sg.Text("ft."),
                   sg.InputText(enable_events=True, size=(3, 2), key="tank_lgth_in"), sg.Text("in.")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("Enter width of liner:")],
                  [sg.InputText(enable_events=True, size=(5, 2), key="tank_wdth_ft"), sg.Text("ft."),
                   sg.InputText(enable_events=True, size=(3, 2), key="tank_wdth_in"), sg.Text("in.")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(6, 1)), sg.Text(size=(34, 2)), sg.Button("Next", size=(6, 1))]]

        # Create window
        window = sg.Window("Quote Calculator", layout)

        # Event reader
        exit_b = self.flat_sheet_config_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false otherwise
        return exit_b

    # Event reader
    def flat_sheet_config_event_reader(self, window, quote):
        # Capture values after next button is pushed
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Next":
                length_ft = float(values["tank_lgth_ft"])
                length_inch = float(values["tank_lgth_in"])
                width_ft = float(values["tank_wdth_ft"])
                width_inch = float(values["tank_wdth_in"])
                quote.lining_system.liner.info.configure(length_ft, length_inch, width_ft, width_inch)
                return False
            if event == "Back":
                return True

    # Creates third window (quote customizations)
    def create_third_window(self, quote):
        # Circular configuration
        if isinstance(quote.lining_system.liner.info, CLiner):
            exit_c = self.create_circular_customizations_window(quote)
        elif isinstance(quote.lining_system.liner.info, RLiner):
            exit_c = self.create_rectangular_customizations_window(quote)
        elif isinstance(quote.lining_system.liner.info, FLiner):
            exit_c = self.create_flat_sheet_customizations_window(quote)
        else:
            exit_c = False
        return exit_c

    # Creates rectangular customizations window
    def create_rectangular_customizations_window(self, quote):
        # Customizations available for rectangular liner
        customizations_available = ["Geo", "Batten Strips", "J-bolts", "Oarlocks",
                                    "Crate(s)", "Leak Detection", "Nailing Strip", "Stainless Clips",
                                    "Lifting Hem", "Installation", "Boots", "Sumps", "Manways",
                                    "Center poles", "Columns", "Add liner(s)", "Discount liner"]

        # Set the layout for customization loop
        layout = [[sg.Text("Choose a customization below:")],
                  [sg.InputCombo(customizations_available, size=(40, 1), enable_events=True,
                                 key="customizations")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(21, 2)), sg.Text("Dashboard:", size=(10, 3))]]
        for order in quote.accessories.orders:
            layout.append([[sg.Text(size=(24, 1)), sg.Text(order.to_string(), size=(10, 1))]])
        layout.append([[sg.Text(size=(40, 2))],
                   [sg.Text(size=(40, 2))],
                   [sg.Button("Back", size=(6, 1)), sg.Text(size=(39, 1)), sg.Button("Choose", size=(6, 1))],
                   [sg.Text(size=(22, 1)), sg.Button("Finish", size=(6, 1))]])

        # Create setup window
        window = sg.Window("Quote Calculator", layout)

        # Event reader
        exit_c = self.customizations_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false otherwise
        return exit_c

    # Creates rectangular customizations window
    def create_flat_sheet_customizations_window(self, quote):
        # Customizations available for flat sheet liner
        customizations_available = ["Geo", "Add liner(s)", "Discount liner"]

        # Set the layout for customization loop
        layout = [[sg.Text("Choose a customization below:")],
                  [sg.InputCombo(customizations_available, size=(40, 1), enable_events=True,
                                 key="customizations")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(21, 2)), sg.Text("Dashboard:", size=(10, 3))]]
        for order in quote.accessories.orders:
            layout.append([[sg.Text(size=(24, 1)), sg.Text(order.to_string(), size=(10, 1))]])
        layout.append([[sg.Text(size=(40, 2))],
                   [sg.Text(size=(40, 2))],
                   [sg.Button("Back", size=(6, 1)), sg.Text(size=(39, 1)), sg.Button("Choose", size=(6, 1))],
                   [sg.Text(size=(22, 1)), sg.Button("Finish", size=(6, 1))]])

        # Create setup window
        window = sg.Window("Quote Calculator", layout)

        # Event reader
        exit_c = self.customizations_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false otherwise
        return exit_c

    # Creates circular customizations window
    def create_circular_customizations_window(self, quote):
        # Customizations available for circular liner
        customizations_available = ["Geo", "Batten Strips", "J-bolts", "Oarlocks",
                                    "Crate(s)", "Leak Detection", "Nailing Strip", "Stainless Clips",
                                    "Lifting Hem", "Installation", "Boots", "Sumps", "Manways",
                                    "Center poles", "Columns", "Add liner(s)", "Discount liner"]
        # Set the layout for customization loop
        layout = [[sg.Text("Choose a customization below:")],
                  [sg.InputCombo(customizations_available, size=(40, 1), enable_events=True,
                                 key="customizations")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(21, 2)), sg.Text("Dashboard:", size=(10, 3))]]
        for order in quote.accessories.orders:
            layout.append([sg.Text(order.to_string())])
        layout.append([[sg.Text(size=(40, 2))],
                   [sg.Text(size=(40, 2))],
                   [sg.Button("Back", size=(6, 1)), sg.Text(size=(39, 1)), sg.Button("Choose", size=(6, 1))],
                   [sg.Text(size=(22, 1)), sg.Button("Finish", size=(6, 1))]])

        # Create setup window
        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_c = self.customizations_event_reader(window)

        # Close window
        window.close()

        # Return true if closed or back, false otherwise
        return exit_c

    # Event reader
    def customizations_event_reader(self, window):
        # Capture values after next button is pushed
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Choose":
                self.customization = values["customizations"].lower()
                return False
            if event == "Back":
                return True
            if event == "Finish":
                return True

    # Updates dashboard of customizations window
    def update(self, quote):
        if isinstance(quote.lining_system.liner.info, CLiner):
            return self.choose_circular_customization_window(quote)

    # Creates fourth window for customization specification of circular tank
    def choose_circular_customization_window(self, quote):
        if self.customization == "geo":
            exit_d = self.create_circular_geo_customization_window(quote)
        elif self.customization == "batten strips":
            exit_d = self.create_circular_batten_strips_customization_window(quote)
        elif self.customization == "j-bolts":
            exit_d = self.create_circular_j_bolts_customization_window(quote)
        elif self.customization == "oarlocks":
            exit_d = self.create_circular_oarlocks_customization_window(quote)
        return exit_d

    # Circular geo customization window
    def create_circular_geo_customization_window(self, quote):
        # Set the layout for geo customization
        layout = [[sg.Text("Enter thickness in ounces: ")],
                  [sg.InputCombo(("8", "16"), enable_events=True, size=(3, 2), key="geo_size"), sg.Text
                  ("oz.")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.circular_geo_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for geo customizations
    def circular_geo_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                wall_thickness = int(values["geo_size"])
                quote.accessories.add_geo(wall_thickness, quote)
                return False
            if event == "Back":
                return True
            if event == "Delete":
                quote.accessories.delete(Geo(0, 0, 0))
                return False

    # Circular batten strip customization window
    def create_circular_batten_strips_customization_window(self, quote):
        layout = [[sg.Text("Choose batten strip type: ")],
                  [sg.InputCombo(("Poly-pro", "Stainless Steel"), enable_events=True, size=(18, 2), key="bs_type")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.circular_batten_strips_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for batten strip customizations
    def circular_batten_strips_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                batten_strip_type = values["bs_type"]
                quote.accessories.add_batten_strip(batten_strip_type,
                                                   quote.lining_system.liner.info.circumference_liner)
                return False
            if event == "Back":
                return True
            if event == "Delete":
                quote.accessories.delete(BattenStrips(0))
                return False

    @staticmethod
    # Circular batten strip customization window
    def create_circular_j_bolts_customization_window(quote):
        quote.accessories.add_j_bolts(quote.lining_system.liner.info.circumference_liner)
        return False

    # Circular oarlocks customization window
    def create_circular_oarlocks_customization_window(self, quote):
        layout = [[sg.Text("How many oarlocks would you like to add: ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="oarlocks_number")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.circular_oarlocks_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for batten strip customizations
    def circular_oarlocks_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                oarlocks_number = int(values["oarlocks_number"])
                quote.accessories.add_oarlocks(oarlocks_number)
                return False
            if event == "Back":
                return True
            if event == "Delete":
                quote.accessories.delete(Oarlocks(0))
                return False

