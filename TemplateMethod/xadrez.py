from jogo import Jogo

class Xadrez(Jogo):
    def __init__(self) -> None:
        super().__init__(2)
        self.quantidade_turnos = 10
        self.turno = 1
        
    def iniciar_jogo(self) -> None:
        print(f"Jogo de Xadrez começou com {self.quantidade_de_jogadores}")
    
    def tem_vencedor(self) -> bool:
        return self.turno == self.quantidade_turnos
    
    def alternar(self) -> None:
        print(f"Turno {self.turno} é a vez do jogador {self.jogador_corrente}")
        self.turno += 1
        self.jogador_corrente = 1 - self.jogador_corrente
    
    def jogador_vencedor(self) -> int:
        return self.jogador_corrente