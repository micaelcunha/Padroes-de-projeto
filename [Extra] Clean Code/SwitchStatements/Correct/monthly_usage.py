from customer import Customer


class MonthlyUsage:
    def __init__(self, customer: Customer, call_minutes: int, sms_count: int) -> None:
        self.customer = customer
        self.call_minutes = call_minutes
        self.sms_count = sms_count