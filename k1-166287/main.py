from vehicle import Vehicle
from car import Car


V_1 = Vehicle()
print(V_1)
V_2 = Vehicle("pomidor",2,2021)
print(V_2)
print(V_1.model)

V_1.pod_year = 1600
print(V_1)

C_1 = Car(12.232,"czerwony",2,"pomidor1",3,2011)
print(C_1)

C_2 = Car(12.232,"czerwony",2,"pomidor1",3,2011)
print(C_2)

print(C_1==C_2)

V_1.pod_year = 1300
print(V_1)
