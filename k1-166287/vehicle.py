

class Vehicle:
    __reg:str
    __model:int
    __pod_year:int
    def __init__(self,reg:str=None,model:int=0,pod_year:int=2022)->None:
        if model <0:
            self.__model = 0
        else:
            self.__model = model
        if 1900 < pod_year >2022:
            self.__pod_year = pod_year
        else:
            self.__pod_year = 2022
        self.__reg = reg
        self.__pod_year = pod_year

    @property
    def reg(self)->str:
        return self.__reg
    @property
    def model(self)->int:
        return self.__model
    @property
    def pod_year(self)->int:
        return self.__pod_year

    @reg.setter
    def reg(self,reg:str)->None:
        self.__reg = reg

    @model.setter
    def model(self,model:int)->None:
        if model <0:
            self.__model = 0
        else:
            self.__model = model

    @pod_year.setter
    def pod_year(self,pod_year:int)->None:
        if 1900 < pod_year > 2022:
            self.__pod_year = pod_year
        else:
            self.__pod_year = 2022
            print("Błędna Wartość")

    def brake(self)->str:
        return f"Zatrzymaj się"

    def drive(self)->str:
        return f"Jade swietnym samochodem z {self.pod_year}"

    def __str__(self)->str:
        return f"Pojazd wyprodukowany w roku: {self.pod_year}\nModel:{self.model}\nRejestracja:{self.reg}\n"
