class Animal:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age
        
    def __str__(self):
        return f'{self.name}, {self.weight} кг, возраст: {self.age}, {self.__class__.__name__}'
        

class Bird(Animal):
    def __init__(self, name, weight, age, view):
        Animal.__init__(self, name, weight, age)
        self.view = view
    
    def fly(self):
        return f'Птица {self.name} умеет летать!'
    
    def __str__(self):
        return f'{super().__str__()} {self.view}'
    
    
class Dog(Animal):
    def __init__(self, name, weight, age, breed, commands):
        Animal.__init__(self, name, weight, age)
        self.breed = breed
        self.commands = commands
    
    def say_commands(self):
        return f'Собака {self.name} знает команды: {self.commands}'
    
    def say_breed(self):
        return f'Собака {self.name} - {self.breed}'
    
    def __str__(self):
        return f'{super().__str__()} {self.breed}, команды: {self.commands}'


class Fish(Animal):
    def __init__(self, name, weight, age, view):
        Animal.__init__(self, name, weight, age)
        self.view = view
    
    def swim(self):
        return f'Рыбка {self.name} плывет'
    
    def __str__(self):
        return f'{super().__str__()} {self.view}'


if __name__ == '__main__':
    fish1 = Fish('Немо', 1, 3, 'клоун')
    dog1 = Dog('Джери', 34, 12, 'немецкая овчарка', ['сидеть', 'голос', 'лежать'])
    bird1 = Bird('Кеша', 0.5, 3, 'ласточка')
    print(bird1)
    print(dog1.say_commands())
    