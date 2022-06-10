# @author Cesar Ramirez
# @program FabsealQuoteCalculator
# @version 2.0


from calculations import *
from accessories import *
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

# Creates first window
exit_a = gui.create_first_window(quote)

while not exit_a:

    # For customizations
    circular = False
    rectangular = False
    lifting_hem = False
    additional_liner_cost = 0
    number_liners = 1

    # ---------------------------------------------------

    # Next page exit button
    exit_b = False

    while not exit_b:

        # Circular tank configuration
        if tank[0] == "c":

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
            window = sg.Window("Quote Calculator", layout)

            # Capture values after next button is pushed
            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    exit_a = True
                    exit_b = True
                    break

                if event == "Next":
                    diameter_ft = float(values["tank_dm_ft"])
                    diameter_inch = float(values["tank_dm_in"])
                    depth_ft = float(values["tank_dp_ft"])
                    depth_inch = float(values["tank_dm_in"])
                    depth_extensions = float(values["tank_dp_ex_in"])
                    break

                if event == "Back":
                    exit_b = True
                    break

            window.close()

            # Check exit
            if exit_b:
                break

            # Diameter configuration
            diameter_tank = converter(diameter_ft, diameter_inch)
            diameter_liner = diameter_modifier(diameter_tank)

            # Depth configuration
            depth_tank = converter(depth_ft, depth_inch)

            # Extra depth extensions
            depth_extensions = converter(0, depth_extensions)
            depth_liner = depth_tank + depth_extensions

            # Extensions
            circumference_tank = diameter_tank * math.pi
            circumference_liner = diameter_liner * math.pi
            circular = True

            # Calculate square footage
            actual_square_footage = circular_tank_sq_footage(diameter_liner, depth_liner)
            # Add the 5%
            five_percent = actual_square_footage * 0.05
            square_footage = round(actual_square_footage + five_percent)

            # Calculate weight of liner
            liner_weight = circular_weight(diameter_liner, depth_liner, weight_sqft)

            # Cost of liner
            liner_cost = square_footage * sqft_price

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
            window = sg.Window("Quote Calculator", layout)

            # Capture values after next button is pushed
            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    exit_a = True
                    exit_b = True
                    break

                if event == "Next":
                    length_ft = float(values["tank_lgth_ft"])
                    length_inch = float(values["tank_lgth_in"])
                    width_ft = float(values["tank_wdth_ft"])
                    width_inch = float(values["tank_wdth_in"])
                    depth_ft = float(values["tank_dp_ft"])
                    depth_inch = float(values["tank_dm_in"])
                    depth_extensions = float(values["tank_dp_ex_in"])
                    break

                if event == "Back":
                    exit_b = True
                    break

            window.close()

            # Check exit
            if exit_b:
                break

            # Length configuration
            length_tank = converter(length_ft, length_inch)
            length_liner = length_modifier(length_tank)

            # Width configuration
            width_tank = converter(width_ft, width_inch)
            width_liner = width_tank

            # Depth configuration
            depth_tank = converter(depth_ft, depth_inch)

            depth_extensions = converter(0, depth_extensions)
            depth_liner = depth_tank + depth_extensions

            # Extensions
            perimeter_tank = (length_tank + width_tank) * 2
            perimeter_liner = (length_liner + width_liner) * 2
            rectangular = True

            # Calculate square footage
            actual_square_footage = rectangular_tank_sq_footage(length_liner, width_liner, depth_liner)
            # Add the 5%
            five_percent = actual_square_footage * 0.05
            square_footage = round(five_percent + actual_square_footage)

            # Calculate weight of liner
            liner_weight = rectangular_weight(length_liner, width_liner, depth_liner, weight_sqft)

            # Cost of liner
            liner_cost = square_footage * sqft_price

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

            # Get circular tank input from user
            layout = [[sg.Text("Enter length of tank:")],
                      [sg.InputText(enable_events=True, size=(5, 2), key="tank_lgth_ft"), sg.Text("ft."),
                       sg.InputText(enable_events=True, size=(3, 2), key="tank_lgth_in"), sg.Text("in.")],
                      [sg.Text(size=(40, 2))],
                      [sg.Text("Enter width of tank:")],
                      [sg.InputText(enable_events=True, size=(5, 2), key="tank_wdth_ft"), sg.Text("ft."),
                       sg.InputText(enable_events=True, size=(3, 2), key="tank_wdth_in"), sg.Text("in.")],
                      [sg.Text(size=(40, 2))],
                      [sg.Text(size=(40, 2))],
                      [sg.Button("Back", size=(6, 1)), sg.Text(size=(34, 2)), sg.Button("Next", size=(6, 1))]]
            window = sg.Window("Quote Calculator", layout)

            # Capture values after next button is pushed
            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    exit_a = True
                    exit_b = True
                    break

                if event == "Next":
                    length_ft = float(values["tank_lgth_ft"])
                    length_inch = float(values["tank_lgth_in"])
                    width_ft = float(values["tank_wdth_ft"])
                    width_inch = float(values["tank_wdth_in"])
                    break

                if event == "Back":
                    exit_b = True
                    break

            window.close()

            # Check exit
            if exit_b:
                break

            # Length configuration
            length_liner = converter(length_ft, length_inch)

            # Width configuration
            width_liner = converter(width_ft, width_inch)

            # Calculate square footage
            square_footage = round(length_liner * width_liner)

            # Calculate weight of liner
            liner_weight = square_footage * weight_sqft

            # Cost of liner
            liner_cost = square_footage * sqft_price

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
