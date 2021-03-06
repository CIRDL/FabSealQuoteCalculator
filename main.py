# @author Cesar Ramirez
# @program FabsealQuoteCalculator
# @version 2.0


from gui_help import *
from document_creator import *


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


# DOCUMENT SECTION

doc = DocumentCreator(quote)

# Creates header paragraph
doc.create_header()

# Creates body
doc.create_general_body()

# Creates calculations body
doc.create_calculations_body()

# Saves document and terminates program
doc.save()
