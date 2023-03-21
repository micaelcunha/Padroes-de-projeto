from customer_type import CustomerType


class Customer:
    def __init__(self, customer_type: CustomerType) -> None:
        self.customer_type = customer_type