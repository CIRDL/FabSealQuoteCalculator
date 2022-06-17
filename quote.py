from accessories import *


# Quote class that contains whole order
class Quote:
    def __init__(self):
        self.lining_system = LiningSystem()
        self.accessories = Accessories()
