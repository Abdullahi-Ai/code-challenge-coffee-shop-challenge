class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer  
        from coffee import Coffee

        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError("Order must be initialized with a Customer instance")

        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError("Order must be initialized with a Coffee instance")

        if isinstance(price, (float, int)) and 1.0 <= float(price) <= 10.0:
            self._price = float(price)
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0")

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price