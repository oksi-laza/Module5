class House:

     def __init__(self, name, floors):
         self.name = name
         self.number_of_floors = floors

     def go_to(self, new_floor):
         if 1 <= new_floor <= self.number_of_floors:
             for i in range(1, new_floor+1):
                 print(i)
         else:
             print(f'{new_floor} - такого этажа не существует')


house1 = House('ЖК Сегодня', 16)
house2 = House('ЖК Европея', 9)
print(house1.name)
house1.go_to(5)
print(house2.name)
house2.go_to(10)