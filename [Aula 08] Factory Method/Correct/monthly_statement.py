from customer import Customer
from customer_type import CustomerType
from monthly_usage import MonthlyUsage


class MonthlyStatement:
    def __init__(self) -> None:
        pass

    def generate(self, monthly_usage: MonthlyUsage) -> Customer:
        if (monthly_usage.customer.customer_type == CustomerType.PAY_AS_YOU_GO):
            return 
        elif (monthly_usage.customer.customer_type == CustomerType.PAY_AS_YOU_GO):
            return
        else:
            raise Exception("The current customer type is not supported")
