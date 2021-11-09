import json


class A(object):
    def __init__(self, a: str):
        self.a = a


class B(object):
    def __init__(self, b: str):
        self.b = b


class Person(A):
    def __init__(self, a: str, name: str, b: B):
        super().__init__(a)
        self.name = name
        self.b = b


if __name__ == '__main__':
    # p = Person("a", "kainhuck", B("b"))
    # print(p.__getattribute__("asdas"))
    # print(p.__init__.__annotations__)
    # print(p.__dict__["b"].__dict__)
    a = {
        "name": None
    }
    print(json.dumps(a))
