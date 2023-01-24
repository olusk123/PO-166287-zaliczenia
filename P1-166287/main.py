from Client import Client
from Potential_buyer import Potential_buyer

k_1 = Client("Nazwa1","jakis adres 1",{'pomidor':1},99)
print(k_1)
print("--------")
k_2 = Client("Nazwa1","jakis adres 2",{'pomidor':2,'pomidr1':4,'pomidor5':6,'pomidor7':8},99)
print(k_2)
print("--------")

print(k_1.__eq__(k_2))
print("--------")
print(k_1.discount())

print("---------------------------------------")
p_1 = Potential_buyer("Nazwa1","jakis adres 1",{'pomider':1},99,100)
print(p_1)
print("-------")
p_2 = Potential_buyer("Nazwa2","jakis adres 2",{'pomider':2},99,100)
print(p_2)
print("------")
print(p_1.is_potential_buyer())


