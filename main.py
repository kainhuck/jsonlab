class Car(object):
    def __init__(self, brand: str):
        self.brand = brand


class Person(object):
    def __init__(self, name: str, car: Car, age, abc: {str:str}, asda:list):
        """
        :param name: str
        :param car: Car
        :param age: asdasdasd
        """
        self.name = name  # name
        self.car = car
        self.age = age


class Demo:
    def __init__(self):
        pass


if __name__ == '__main__':
    print(type(Person.__init__.__annotations__["abc"]))
    print(type(Person.__init__.__annotations__["asda"]))
    print(isinstance(Person.__init__.__annotations__["abc"], type))
    print(isinstance(Person.__init__.__annotations__["asda"], type))
