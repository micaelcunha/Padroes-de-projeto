from customer_type import CustomerType
from monthly_usage import MonthlyUsage


class MonthlyStatement:
    def __init__(self) -> None:
        self.call_cost: float
        self.sms_cost: float
        self.total_cost: float

    def generate(self, monthly_usage: MonthlyUsage):
        if (monthly_usage.customer.customer_type == CustomerType.PAY_AS_YOU_GO):
            self.call_cost = 0.12 * monthly_usage.call_minutes
            self.sms_cost = 0.12 * monthly_usage.sms_count
            self.total_cost = self.call_cost + self.sms_cost
        elif (monthly_usage.customer.customer_type == CustomerType.PAY_AS_YOU_GO):
            self.total_cost = 54.90
        else:
            raise Exception("The current customer type is not supported")
