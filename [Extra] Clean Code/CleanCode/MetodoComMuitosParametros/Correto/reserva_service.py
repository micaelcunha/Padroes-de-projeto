import datetime
from reserva import Reserva
from reserva_data_query import ReservaDataQuery

from usuario import Usuario


class ReservaService:
    def __init__(self) -> None:
        pass
    
    def buscar_reserva(self,
                      usuario: Usuario,
                      reserva_data_query: ReservaDataQuery,
                      cliente_id: int = None) -> Reserva:
        pass
    
    def buscar_reserva_com_promocao(self,
                      reserva_data_query: ReservaDataQuery,
                      usuario: Usuario,
                      promocao_id: int) -> Reserva:
        pass
    
    def criar_reserva(self,
                      reserva_data_query: ReservaDataQuery,
                      local_id: int):
        pass