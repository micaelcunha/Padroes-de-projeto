from builder import Builder


class Director:
    def __init__(self) -> None:
        self.__builder = None

    @property
    def builder(self) -> Builder:
        return self.__builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self.__builder = builder

    def build_minimal_viable_product(self) -> None:
        self.__builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.__builder.produce_part_a()
        self.__builder.produce_part_b()
        self.__builder.produce_part_c()
