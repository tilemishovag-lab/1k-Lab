class Person:
    def __init__(self, name, age, height, education):
        self.name = name
        self.age = age
        self.height = height
        self.edu = education

    def singer(self, song):
        return f'This person can - sing {song}'

    def __str__(self):
        return f'Имя - {self.name}\nВозраст - {self.age}\nРост - {self.height}\nОбразование - {self.edu}'

person1 = Person(name='Rasul', age=18, height=180, education=False)
person2 = Person(name='Malika', age=15, height=170, education=True)
print(person1)
print(person1.singer('Jungle bells'))
print(person2)
print(person2.singer('Fade to Black'))


class Children(Person):
    def __init__(self, name, age, height, education, car, house):
        super().__init__(name, age, height, education)
        self.car = car
        self.house = house

    def __str__(self):
        return super().__str__()+f'\nCar - {self.car}\nHouse - {self.house}'


child1 = Children(name='Ruslan', age=9, height=140, education=False, car='Lamborgini', house=True)
print(child1)
print(child1.singer('Nothing'))
