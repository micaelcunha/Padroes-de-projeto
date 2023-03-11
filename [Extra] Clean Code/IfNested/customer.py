class Customer:
    def __init__(self, loyalty_points: int) -> None:
        self.loyalty_points = loyalty_points

    
    def tem_fidelizacao(self, points) -> bool:
        return (self.loyalty_points > points)