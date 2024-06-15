class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Новое количество этажей: {self.numberOfFloors}')


house1 = House()
house1.setNewNumberOfFloors(16)

house2 = House()
house2.setNewNumberOfFloors(5)