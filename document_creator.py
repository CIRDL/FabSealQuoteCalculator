import quote
from quote import *
import docx
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.text import WD_LINE_SPACING
from docx.enum.text import WD_UNDERLINE
from datetime import date
from num2words import num2words


class DocumentCreator:
    def __init__(self, quote):
        self.quote = quote
        self.today_date = date.today().strftime("%B %d, %Y")
        self.doc = docx.Document()

    # Creates header section of document
    def create_header(self):
        # Create header paragraph for quote
        header = self.doc.add_paragraph(self.today_date)
        header.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

        # Fill out important info
        header.add_run('\nNAME OF CONTACT')
        header.add_run('\nCOMPANY NAME')
        header.add_run('\nPHONE NUMBER')
        header.add_run('\nZip Code: FILL OUT HERE')
        header.add_run('\nCITY, STATE')

        # Double spacing for header
        header.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE

    # Creates general body of document
    def create_general_body(self):
        # Records liner information
        body_string = num2words(self.doc.lining_system.total_liners).capitalize() + \
                      f"({self.quote.lining_system.total_liners}) liner"
        if self.quote.lining_system.total_liners > 1:
            body_string += "s"
        body_string += " fabricated from ENTER MATERIAL NAME HERE"
        body = self.doc.add_paragraph(body_string)
        self.__dimensions_info(body)

    # Prints out dimensions based on tank shape
    def __dimensions_info(self, body):
        ref_liner = self.quote.lining_system.liner.info
        if isinstance(ref_liner, CLiner):
            body.add_run(f'\n\n{feet_deconverter(ref_liner.diameter_tank)}\''
                         f'-{inch_deconverter(ref_liner.diameter_tank)}\" diameter '
                         f'X {feet_deconverter(ref_liner.depth_tank)}\'-{inch_deconverter(ref_liner.depth_tank)}\" '
                         f'deep')
            if ref_liner.depth_liner - ref_liner.depth_tank > 0:
                body.add_run(" with ENTER DEPTH EXTENSIONS HERE. ")
            else:
                body.add_run(". ")

    # Prints out customizations to general body
    def __customizations_info(self, body):
        # Temp variable for shorter reference
        order_list = self.quote.accessories.orders
        # Iterates through order list if needed
        if len(order_list) > 0:
            body.add_run(f'Includes ')
            # Loops through order list to add customizations to general body
            for order in order_list:
                # Sneaks in 'and'
                if order_list[-1] == order and len(order_list) > 1:
                    body.add_run(f'and ')

                # Geo
                if order[0] == 'g' and order[1] == 'e':
                    if circular or rectangular:
                        body.add_run(
                            f'16oz geotextile padding for the floor and {geo_material_type}oz geotextile padding for the '
                            f'sidewalls')
                        if order_list.index(order) != len(order_list) - 1:
                            body.add_run(", ")
                    else:
                        geo_set = set(geo_list)
                        for material in geo_set:
                            geo_count = 0
                            for geo in geo_list:
                                if geo == material:
                                    geo_count += 1
                            body.add_run(f"{num2words(geo_count)} ({geo_count}) layers of {material}oz geo")
                            if order_list.index(order) != len(order_list) - 1:
                                body.add_run(", ")

    # Saves quote and terminates program
    def save(self):
        self.doc.save("Quote.docx")
