from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """
        Getter для получения значения атрибута number_of_sim.
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Setter для установки значения атрибута number_of_sim.
        """
        if value < 0:
            raise ValueError("Количество сим-карт не может быть отрицательным")
        self._number_of_sim = value

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"