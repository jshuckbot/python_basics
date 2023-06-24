from animals import Bird, Dog, Fish


class FablicAninal:
    __animals = {'dog': Dog, 'bird': Bird, 'fish': Fish}
    
    @staticmethod
    def create_animal(class_animal, *args, **kwargs):
        return FablicAninal.__animals[class_animal.lower()](*args, **kwargs)


if __name__ == '__main__':
    dog = FablicAninal.create_animal('dog', 'Джери', 5, 23, 'немецкая овчарка', ['сидеть', 'голос'])
    print(dog)
    