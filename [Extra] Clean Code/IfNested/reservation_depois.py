import datetime

from customer import Customer


class Reservation:
    def __init__(self, customer: Customer, date_time: datetime) -> None:
        self.customer = customer
        self.date_time = date_time
        self.is_canceled: bool = False

    def data_valida(self, maximo_de_horas) -> bool:
        return ((self.date_time - datetime.now()).TotalHours < maximo_de_horas)

    def verifique_elegibilidade(self) -> bool:
        return (((self.customer.tem_fidelizacao(100)) and (self.data_valida(24)))
                 or 
                ((not self.customer.tem_fidelizacao(100)) and (self.data_valida(48))))
    
    def cancel(self):
        if(self.verifique_elegibilidade()):
            self.is_canceled = True
            return
        
        raise Exception("It's too late to cancel.")
            
