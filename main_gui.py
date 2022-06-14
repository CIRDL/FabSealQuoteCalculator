# @author Cesar Ramirez
# @program FabsealQuoteCalculator
# @version 2.0


from gui_help import *
from error import *
import docx
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.text import WD_LINE_SPACING
from docx.enum.text import WD_UNDERLINE
from datetime import date
from num2words import num2words


# Create GuiHelp object
gui = GuiHelp()

# Create Quote object
quote = Quote()

# Page exit button
exit_a = False

# Creates loop to allow for back button
while not exit_a:

    # Creates first window for liner setup
    exit_a = gui.create_first_window(quote)

    # Next page exit button
    exit_b = False

    # Loop for back button
    while not exit_b:

        # Creates second window for liner customizations
        exit_b = gui.create_second_window(quote)

        # Configures information from second window into customized liner order
        quote.lining_system.liner.configure()

        # Next page exit button
        exit_c = False

        # Loop for back button
        while not exit_c:

            # Creates third window for quote customizations
            exit_c = gui.create_third_window(quote)

            # quote.configure()


        # circular path
        if tank[0] == "c":

            # Setup for customization loop
            total_quote_cost = liner_cost
            total_mobilization_cost = 0
            lining_system_cost = liner_cost
            total_weight = liner_weight
            total_liners = 1
            order_list = []
            satisfied = False
            discounted = False
            installation_included = False
            crate_included = False
            customizations_available = ["Geo", "Batten Strips", "J-bolts", "Oarlocks",
                                           "Crate(s)", "Leak Detection", "Nailing Strip", "Stainless Clips",
                                           "Lifting Hem", "Installation","Boots", "Sumps", "Manways",
                                           "Center poles", "Columns", "Add liner(s)", "Discount liner"]

            # -----------------------------------------------

            # Next page exit button
            exit_c = False

            # For dashboard
            dashboard = ""

            while not exit_c:

                # Set the layout for customization loop
                layout = [[sg.Text("Choose a customization below:")],
                          [sg.InputCombo(customizations_available, size=(40, 1), enable_events=True,
                                         key="customizations")],
                          [sg.Text(size=(40, 2))],
                          [sg.Text(size=(21, 2)), sg.Text("Dashboard:", size=(10, 3))]]
                for order in order_list:
                    layout += [sg.Text(size=(24, 2)), sg.Text(order, size=(10, 3))]
                layout += [[sg.Text(size=(40, 2))],
                          [sg.Text(size=(40, 2))],
                          [sg.Button("Back", size=(6, 1)), sg.Text(size=(39, 1)), sg.Button("Choose", size=(6, 1))],
                          [sg.Text(size=(23, 1)), sg.Button("Finish", size=(6, 1))]]

                # Create setup window
                setup_window = sg.Window("Quote Customizations", layout)

                while True:
                    event, values = setup_window.read()
                    if event == sg.WINDOW_CLOSED:
                        exit_a = True
                        exit_b = True
                        exit_c = True
                        break

                    if event == "Choose":
                        customization = values["customizations"].lower()
                        # Keep track of order
                        order_list.append(customization)
                        break

                    if event == "Back":
                        exit_b = False
                        exit_c = True
                        break

                    if event == "Finish":
                        break

                setup_window.close()

                # Check exit
                if exit_c:
                    break

                # -------------------------------------------------

                # Next page exit button
                exit_d = False

                while not exit_d:

                    if customization[0] == "g" and customization[1] == "e":
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

                        while True:
                            event, values = window.read()
                            if event == sg.WINDOW_CLOSED:
                                break

                            if event == "Add":
                                geo_material_type = int(values["geo_size"])

                            if event == "Back":
                                exit_c = False
                                exit_d = True
                                break

                        window.close()

                        total_geo_cost = geo_cost_circular(geo_material_type, wall_circular_tank_sq_footage
                        (diameter_liner, depth_liner), floor_circular_tank_sq_footage(diameter_liner))
                        total_geo_weight = geo_weight_circular(geo_material_type, diameter_tank, depth_tank)

                        # Quote documentation
                        lining_system_cost += total_geo_cost

                        # Calculates total costs and weights
                        total_quote_cost += total_geo_cost
                        total_weight += total_geo_weight

            # Update dashboard

            # Return to customizations homepage


        # Rectangular tank configuration
        if tank[0] == "r":

            # Setup for customization loop
            total_quote_cost = liner_cost
            total_mobilization_cost = 0
            lining_system_cost = liner_cost
            total_weight = liner_weight
            total_liners = 1
            order_list = []
            satisfied = False
            discounted = False
            installation_included = False
            crate_included = False
            customizations_available = ["Geo", "Batten Strips", "J-bolts", "Oarlocks",
                                           "Crate(s)", "Leak Detection", "Nailing Strip", "Stainless Clips",
                                           "Lifting Hem", "Installation","Boots", "Sumps", "Manways",
                                           "Center poles", "Columns", "Add liner(s)", "Discount liner"]

            # -----------------------------------------------

            # Next page exit button
            exit_c = False

            while not exit_c:

                # Set the layout for customization loop
                layout = [[sg.Text("Choose a customization below:")],
                          [sg.InputCombo(customizations_available, size=(40, 1), enable_events=True,
                                         key="customizations")],
                          [sg.Text(size=(40, 2))],
                          [sg.Text(size=(40, 2))],
                          [sg.HorizontalSeparator()]
                          [sg.Text("Dashboard:")],
                          [sg.Text(size=(40, 2))],
                          [sg.Text(size=(40, 2))],
                          [sg.Button("Back", size=(6, 1)), sg.Text(size=(40, 1)), sg.Button("Next", size=(6, 1))],
                          [sg.Text(size=(36, 1)), sg.Button("Finish")]]

                # Create setup window
                setup_window = sg.Window("Quote Calculator", layout)

                while True:
                    event, values = setup_window.read()
                    if event == sg.WINDOW_CLOSED:
                        exit_a = True
                        break

                    if event == "Next":
                        tank = values["tank_type"].lower()
                        sqft_price = float(values["square_foot_cost"])
                        weight_sqft = float(values["square_foot_weight"])
                        break

                setup_window.close()

                # Check exit
                if exit_a and exit_b:
                    break




        # Flat sheet configuration
        if tank[0] == "f":

            # Setup for customization loop
            total_quote_cost = liner_cost
            total_mobilization_cost = 0
            lining_system_cost = liner_cost
            total_weight = liner_weight
            total_liners = 1
            order_list = []
            satisfied = False
            discounted = False
            installation_included = False
            crate_included = False
            customizations_available = ["Geo", "Add liner(s)", "Discount liner"]

            # -----------------------------------------------

            # Next page exit button
            exit_c = False

            while not exit_c:

                # Set the layout for customization loop
                layout = [[sg.Text("Choose a customization below:")],
                          [sg.InputCombo(customizations_available, size=(40, 1), enable_events=True,
                                         key="customizations")],
                          [sg.Text(size=(40, 2))],
                          [sg.Text(size=(40, 2))],
                          [sg.HorizontalSeparator()]
                          [sg.Text("Dashboard:")],
                          [sg.Text(size=(40, 2))],
                          [sg.Text(size=(40, 2))],
                          [sg.Button("Back", size=(6, 1)), sg.Text(size=(40, 1)), sg.Button("Next", size=(6, 1))],
                          [sg.Text(size=(36, 1)), sg.Button("Finish")]]

                # Create setup window
                setup_window = sg.Window("Quote Calculator", layout)

                while True:
                    event, values = setup_window.read()
                    if event == sg.WINDOW_CLOSED:
                        exit_a = True
                        break

                    if event == "Next":
                        tank = values["tank_type"].lower()
                        sqft_price = float(values["square_foot_cost"])
                        weight_sqft = float(values["square_foot_weight"])
                        break

                setup_window.close()

                # Check exit
                if exit_a and exit_b:
                    break
