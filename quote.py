class Quote:



    def __init__(self, tank, sqft_price, weight_sqft):
        self.tank = tank
        self.sqft_price = sqft_price
        self.weight_sqft = weight_sqft
        # For customizations
        self.circular = False
        self.rectangular = False
        self.lifting_hem = False
        self.additional_liner_cost = 0
        self.number_liners = 1

    def ()