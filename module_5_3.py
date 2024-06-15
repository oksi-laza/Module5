class Building:
    def __init__(self, floors, buildingType):
        self.numberOfFloors = floors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building_dream = Building(25, 'Монолитно-кирпичное строение')
building_story = Building(16, 'Железобетонное строение')
building_life = Building(25, 'Монолитно-кирпичное строение')
print('ЖК Мечта и ЖК История равнозначны по некоторым характеристикам:', building_dream == building_story)
print('ЖК История и ЖК Жизнь равнозначны по некоторым характеристикам:', building_story == building_life)
print('ЖК Жизнь и ЖК Мечта равнозначны по некоторым характеристикам:', building_life == building_dream)