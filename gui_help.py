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
                                    "Crate", "Leak Detection", "Nailing Strips", "Stainless Clips",
                                    "Lifting Hem", "Installation", "Boots", "Sumps", "Manways",
                                    "Center poles", "Columns", "Add liner(s)", "Discount liner"]
        # Set the layout for customization loop
        layout = [[sg.Text("Choose a customization below:")],
                  [sg.InputCombo(customizations_available, size=(40, 1), enable_events=True,
                                 key="customizations")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(21, 2)), sg.Text("Dashboard:", size=(10, 3))]]
        for order in quote.accessories.orders:
            if isinstance(order, type("")):
                if order[0].lower() == "l":
                    layout.append([sg.Button("Lifting hem")])
                elif order[0].lower() == "a":
                    layout.append([sg.Button(order)])
                elif order[0].lower() == "d":
                    layout.append([sg.Button(order)])
            else:
                layout.append([sg.Button(order.to_string())])
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
                self.exit = True
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
        elif self.customization == "crate":
            exit_d = self.create_crate_customization_window(quote)
        elif self.customization == "leak detection":
            exit_d = self.create_circular_leak_detection_customization_window(quote)
        elif self.customization == "nailing strips":
            exit_d = self.create_nailing_strips_customization_window(quote)
        elif self.customization == "stainless clips":
            exit_d = self.create_stainless_clips_customization_window(quote)
        elif self.customization == "lifting hem":
            exit_d = self.create_lifting_hem_customization_window(quote)
        elif self.customization == "installation":
            exit_d = self.create_circular_installation_package_customization_window(quote)
        elif self.customization == "boots":
            exit_d = self.create_boot_customization_window(quote)
        elif self.customization == "sumps":
            exit_d = self.create_sump_customization_window(quote)
        elif self.customization == "manways":
            exit_d = self.create_manway_customization_window(quote)
        elif self.customization == "center poles":
            exit_d = self.create_center_pole_customization_window(quote)
        elif self.customization == "columns":
            exit_d = self.create_column_customization_window(quote)
        elif self.customization == "add liner(s)":
            exit_d = self.create_add_liner_customization_window(quote)
        elif self.customization == "discount liner":
            exit_d = self.create_discount_liner_customization_window(quote)
        return exit_d

    # Discount liner customization window
    def create_discount_liner_customization_window(self, quote):
        # Set the layout for discount liner customization
        layout = [[sg.Text("Enter discount percentage for liner: ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="discount_percentage"), sg.Text("%")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.discount_liner_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for manway customization window
    def discount_liner_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                discount_percentage = int(values["discount_percentage"])
                quote.accessories.discount_liner(quote, discount_percentage)
                return False
            if event == "Back":
                return True

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

    # Crate customization window
    def create_crate_customization_window(self, quote):
        # Set the layout for crate customization
        layout = [[sg.Text("Enter crate size: ")],
                  [sg.InputCombo(("Small", "Large"), enable_events=True, size=(8, 2), key="crate_size")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("How many would you like?")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="number_crates")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.crate_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for crate customizations
    def crate_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                size = values["crate_size"]
                number_crates = int(values["number_crates"])
                for i in range(number_crates):
                    quote.accessories.add_crate(size)
                return False
            if event == "Back":
                return True
            if event == "Delete":
                quote.accessories.delete(Crate("Default"))
                return False

    @staticmethod
    # Circular leak detection customization window
    def create_circular_leak_detection_customization_window(quote):
        quote.accessories.add_leak_detection(quote.lining_system.liner.info.circumference_liner)
        return False

    @staticmethod
    # Circular nailing strip customization window
    def create_nailing_strips_customization_window(quote):
        quote.accessories.add_nailing_strips(quote.lining_system.liner.info.circumference_liner)
        return False

    @staticmethod
    # Circular stainless2 clips customization window
    def create_stainless_clips_customization_window(quote):
        quote.accessories.add_stainless_clips(quote.lining_system.liner.info.circumference_liner)
        return False

    @staticmethod
    # Circular lifting hem customization window
    def create_lifting_hem_customization_window(quote):
        quote.accessories.add_lifting_hem(quote)
        return False

    # Circular installation customization window
    def create_circular_installation_package_customization_window(self, quote):
        # Set the layout for installation customization
        layout = [[sg.Text("Is the site survey within the US? ")],
                  [sg.InputCombo(("Yes", "No"), enable_events=True, size=(4, 2), key="within_USA")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Next", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.circular_installation_package_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for installation package customizations
    def circular_installation_package_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Next":
                within_usa = values["within_USA"].lower()
                customized_site_survey = False
                if within_usa[0] == "y":
                    # Returns True if exit or back, yes and no to answer question otherwise
                    is_within_600_miles = self.circular_installation_within_usa_window()
                    if isinstance(is_within_600_miles, bool):
                        return True
                else:
                    is_within_600_miles = "no"
                    customized_site_survey = True
                    # Returns True if exit or back, float otherwise
                    site_survey_cost = self.installation_site_survey_cost_window()
                # Returns True if exit or back, float otherwise
                traveling_cost = self.circular_installation_traveling_cost_window()
                if isinstance(traveling_cost, bool):
                    return True
                quote.accessories.add_installation_package(within_usa, is_within_600_miles, traveling_cost,
                                                           quote.lining_system)
                if customized_site_survey:
                    quote.accessories.orders[len(quote.accessories.orders) - 1].set_site_survey_cost(site_survey_cost)
                return False
            if event == "Back":
                return True

    # Circular installation within USA customization window
    def circular_installation_within_usa_window(self):
        layout = [[sg.Text("Is the site survey within 600 miles? ")],
                  [sg.InputCombo(("Yes", "No"), enable_events=True, size=(4, 2), key="within_600")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Next", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.circular_installation_within_usa_event_reader(window)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for installation package customizations
    def circular_installation_within_usa_event_reader(self, window):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Next":
                within_usa = values["within_600"].lower()
                if within_usa[0] == "y":
                    return "yes"
                else:
                    return "no"
            if event == "Back":
                return True

    # Asks for site survey cost in the case that project is outside of USA
    def installation_site_survey_cost_window(self):
        layout = [[sg.Text("Enter cost of site survey: ")],
                  [sg.Text("$"), sg.InputText(enable_events=True, key="site_survey_cost", size=(10, 1))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Next", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        site_survey_cost = self.installation_site_survey_event_reader(window)

        # Close window
        window.close()

        # Return true if closed or back, traveling cost float if otherwise
        return site_survey_cost

    # Event reader for customized site survey
    def installation_site_survey_event_reader(self, window):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Next":
                return float(values["site_survey_cost"])
            if event == "Back":
                return True

    # Circular installation within USA customization window
    def circular_installation_traveling_cost_window(self):
        layout = [[sg.Text("Enter cost of traveling: ")],
                  [sg.Text("$"), sg.InputText(enable_events=True, key="traveling_cost", size=(10, 1))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Next", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        traveling_cost = self.circular_installation_traveling_cost_event_reader(window)

        # Close window
        window.close()

        # Return true if closed or back, traveling cost float if otherwise
        return traveling_cost

    # Event reader for installation package customizations
    def circular_installation_traveling_cost_event_reader(self, window):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Next":
                return float(values["traveling_cost"])
            if event == "Back":
                return True

    # Boots customization window
    def create_boot_customization_window(self, quote):
        layout = [[sg.Text("Enter boot size in inches: ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="boot_size")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("How many would you like? ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="number_boots")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.boot_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for batten strip customizations
    def boot_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                boot_size = float(values["boot_size"])
                number_boots = int(values["number_boots"])
                for i in range(number_boots):
                    quote.accessories.add_boot(boot_size)
                return False
            if event == "Back":
                return True
            if event == "Delete":
                quote.accessories.delete(Boot(0))
                return False

    # Sump customization window
    def create_sump_customization_window(self, quote):
        layout = [[sg.Text("Enter square footage of material used for sump: ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="square_footage")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("How many would you like? ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="number_sumps")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.sump_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for sump customization window
    def sump_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                square_footage = float(values["square_footage"])
                number_sumps = int(values["number_sumps"])
                for i in range(number_sumps):
                    quote.accessories.add_sump(square_footage, quote.lining_system.liner.sq_price)
                return False
            if event == "Back":
                return True
            if event == "Delete":
                quote.accessories.delete(Sump(0, 0))
                return False

    # Manway customization window
    def create_manway_customization_window(self, quote):
        layout = [[sg.Text("Enter square footage of material used for manway: ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="square_footage")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("How many would you like? ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="number_manways")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.manway_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for manway customization window
    def manway_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                square_footage = float(values["square_footage"])
                number_manways = int(values["number_manways"])
                for i in range(number_manways):
                    quote.accessories.add_manway(square_footage, quote.lining_system.liner.sq_price)
                return False
            if event == "Back":
                return True
            if event == "Delete":
                quote.accessories.delete(ManWay(0, 0))
                return False

    # Center pole customization window
    def create_center_pole_customization_window(self, quote):
        layout = [[sg.Text("Enter square footage of material used for center pole: ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="square_footage")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("How many would you like? ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="number_center_poles")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.center_pole_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for center pole customization window
    def center_pole_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                square_footage = float(values["square_footage"])
                number_center_poles = int(values["number_center_poles"])
                for i in range(number_center_poles):
                    quote.accessories.add_center_pole(square_footage, quote.lining_system.liner.sq_price)
                return False
            if event == "Back":
                return True
            if event == "Delete":
                quote.accessories.delete(CenterPole(0, 0))
                return False

    # Column customization window
    def create_column_customization_window(self, quote):
        layout = [[sg.Text("Enter square footage of material used for column: ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="square_footage")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text("How many would you like? ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="number_columns")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.column_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for column customization window
    def column_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                square_footage = float(values["square_footage"])
                number_columns = int(values["number_columns"])
                for i in range(number_columns):
                    quote.accessories.add_column(square_footage, quote.lining_system.liner.sq_price)
                return False
            if event == "Back":
                return True
            if event == "Delete":
                quote.accessories.delete(Column(0, 0))
                return False

    # Add liner customization window
    def create_add_liner_customization_window(self, quote):
        # Set the layout for liner addition customization
        layout = [[sg.Text("How many liners would you like to add? ")],
                  [sg.InputText(enable_events=True, size=(6, 2), key="additional_liners")],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Text(size=(40, 2))],
                  [sg.Button("Back", size=(4, 1)), sg.Text(size=(31, 1)), sg.Button("Add", size=(6, 1))]]

        window = sg.Window("Quote Customizations", layout)

        # Event reader
        exit_d = self.add_liner_customization_event_reader(window, quote)

        # Close window
        window.close()

        # Return true if closed or back, false if add or delete
        return exit_d

    # Event reader for add liner customization window
    def add_liner_customization_event_reader(self, window, quote):
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                self.exit = True
                return True
            if event == "Add":
                additional_liners = int(values["additional_liners"])
                quote.accessories.add_liners(quote, additional_liners)
                return False
            if event == "Back":
                return True
