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
while not exit_a and not gui.exit:

    # Creates first window for liner setup
    exit_a = gui.create_first_window(quote)

    # Back button
    if exit_a:
        break

    # Next page exit button
    exit_b = False

    # Loop for back button
    while not exit_b and not gui.exit:

        # Creates second window for liner customizations
        exit_b = gui.create_second_window(quote)

        # Back button
        if exit_b:
            break

        # Configures information from second window into customized liner order
        quote.lining_system.liner.configure()

        # Next page exit button
        exit_c = False

        # Loop for back button
        while not exit_c and not gui.exit:

            # Creates third window for quote customizations
            exit_c = gui.create_third_window(quote)

            # Back button
            if exit_c:
                break

            # Updates dashboard of quote
            gui.update(quote)
