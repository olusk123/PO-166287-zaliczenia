import sys



class Client:
    __name: str
    __adress: str
    __items_bought: dict[str, int]
    __bill: float

    def __init__(self, name: str, adress: str, items_bought: dict[str, int] == {}, bill: float = 0):
        self.__name = name
        self.__adress = adress
        if bill < 0:
            self.__bill = 0
        else:
            self.__bill = bill
        self.__items_bought = items_bought
        if self.__items_bought.keys() < {0}:
            print("nieprawidlowa wartosc")
            sys.exit(-10)
        if len(self.__items_bought) > 0 and self.__bill <= 0:
            print("nieprawidlowa wartosc")
            sys.exit(-20)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def adress(self) -> str:
        return self.__adress

    @adress.setter
    def adress(self, address: str) -> None:
        self.__adress = address

    @property
    def items_bought(self) -> dict[str,int]:
        return self.__items_bought

    @items_bought.setter
    def items_bought(self, value: dict[str, int])->None:
        if self.__items_bought.keys() < {0}:
            print("nieprawidlowa wartosc")
            sys.exit(-10)
        elif len(self.__items_bought) > 0:
            print("nieprawidlowa wartosc")
            sys.exit(-20)
        else:
            self.__items_bought = value

    @property
    def bill(self) -> float:
        return self.__bill

    @bill.setter
    def bill(self, value: float) -> None:
        if value < 0:
            self.__bill = 0
        else:
            self.__bill = value

    def discount(self):
        for item in self.items_bought:
            if self.__items_bought[item] > 3:
                return (self.__bill * 1.2)/100
            elif self.__bill > 200:
                return (self.__bill * 3.7)/100
            else:
                return 'brak'

    def __str__(self)->str:
        if len(self.__items_bought) == 0:
            return f"Nazwa klasy: {self.__name}\n" \
                f"Adres: {self.__adress}\n"
        else:
            return f"Nazwa klasy: {self.__name}\n" \
                   f"Adres: {self.__adress}\n" \
                   f"kupione przedmioty: {self.__items_bought}\n" \
                   f"Rachunek: {self.__bill} zł"


    def __eq__(self, other) -> bool:
        if self.__name == other.__name:
            return True
        else:
            return self.__adress == other.__adress



