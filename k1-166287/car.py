from vehicle import Vehicle


class Car(Vehicle):
    __price: float
    __colour: str
    __extra_seats: int

    def __init__(self, price: float = 0, colour: str = None, extra_seats: int = 0,reg:str=None, model:int=0, pod_year:int=2022) -> None:
        super().__init__(reg,model,pod_year)
        self.__colour = colour
        if price < 0:
            self.__price = price
            print("Błędna wartosc")
        else:
            self.__price = 0
        if extra_seats < 0:
            self.__extra_seats = extra_seats
            print("Błędna wartosc")
        else:
            self.__extra_seats = 0

    @property
    def price(self) -> float:
        return self.__price

    @property
    def colour(self) -> str:
        return self.__colour

    @property
    def extra_seats(self) -> int:
        return self.__extra_seats

    @price.setter
    def price(self, price:float) -> None:
        if price < 0:
            self.__price = price
            print("Błędna wartosc")
        else:
            self.__price = 0

    @colour.setter
    def colour(self, colour:str) -> None:
        self.__colour = colour

    @extra_seats.setter
    def extra_seats(self, extra_seats:int) -> None:
        if extra_seats < 0:
            self.__extra_seats = extra_seats
            print("Błędna wartosc")
        else:
            self.__extra_seats = 0

    def drive(self) -> str:
        return f"Jade swietnym samochodem z {self.pod_year}! Ma Kolor:{self.colour}"

    def __eq__(self, __other: Vehicle) -> None:
        return self.price == __other.price and self.model == __other.model

    def __ne__(self, __other: Vehicle) -> None:
        return self.price != __other.price and self.model != __other.model
    def __str__(self)->str:
        return f"Pojazd wyprodukowany w roku:{self.pod_year}\nModel:{self.model}\nRejestracja:{self.reg}\n" \
               f"Cena:{self.price}\nKolor:{self.colour}\nDodatkowe siedzenia: {self.extra_seats}\n"
