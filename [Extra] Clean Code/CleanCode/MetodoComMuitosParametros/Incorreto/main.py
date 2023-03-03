from reserva_service import ReservaService
from usuario import Usuario


reserva_service = ReservaService()


reserva_service.buscar_reserva_com_promocao("10/10/2023", "12/10/2023", Usuario("Eduardo"), 10, 10)