from Client import Client
import sys


class Potential_buyer(Client):
    __discount_limit: float

    def __init__(self, name: str, adress: str, items_bought: dict[str, int], bill: float = 0,
                 discount_limit: float = 100):
        super().__init__(name, adress, items_bought, bill)
        self.__discount_limit = discount_limit
        if discount_limit < 100:
            print("niepoprawna wartosc")
            sys.exit(-10)

    @property
    def discount_limit(self) -> float:
        return self.__discount_limit

    @discount_limit.setter
    def discount_limit(self, value: float) -> None:
        if value < 100:
            print("niepoprawna wartosc")
            sys.exit(-10)
        self.__discount_limit = value

    def is_potential_buyer(self) -> bool:
        for item in self.items_bought:
            if self.items_bought[item] > 3:
                if (self.bill * 1.2) / 100 > self.__discount_limit:
                    return True
                else:
                    return False
            elif self.bill > 200:
                if (self.bill * 1.2) / 100 > self.__discount_limit:
                    return True
                else:
                    return False
            else:
                return False
