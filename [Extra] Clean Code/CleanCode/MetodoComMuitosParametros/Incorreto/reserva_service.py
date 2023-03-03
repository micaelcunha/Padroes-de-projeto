import datetime
from reserva import Reserva

from usuario import Usuario


class ReservaService:
    def __init__(self) -> None:
        pass
    
    def buscar_reserva(self,
                      data_ida: datetime,
                      data_volta: datetime,
                      usuario: Usuario,
                      local_id: int,
                      cliente_id: int = None) -> Reserva:
        pass
    
    def buscar_reserva_com_promocao(self,
                      data_ida: datetime,
                      data_volta: datetime,
                      usuario: Usuario,
                      local_id: int,
                      promocao_id: int) -> Reserva:
        pass
    
    def criar_reserva(self,
                      data_ida: datetime,
                      data_volta: datetime,
                      local_id: int):
        pass