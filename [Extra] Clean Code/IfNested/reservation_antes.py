import datetime

from customer import Customer


class Reservation:
    def __init__(self, customer: Customer, date_time: datetime) -> None:
        self.customer = customer
        self.date_time = date_time
        self.is_canceled: bool = False

    def cancel(self) -> bool:
        if (self.customer.loyalty_points > 100):
            if (datetime.now() > self.date_time):
                raise Exception("It's too late to cancel.")
            elif ((self.date_time - datetime.now()).TotalHours < 24):
                raise Exception("It's too late to cancel.")
            
            self.is_canceled = True
        else:
            if (datetime.now() > self.date_time):
                raise Exception("It's too late to cancel.")
            elif ((self.date_time - datetime.now()).TotalHours < 48):
                raise Exception("It's too late to cancel.")
            
            self.is_canceled = True


            
