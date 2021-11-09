from jsonparser import marshal


# 类的属性都是基本类型
def test1():
    class Person(object):
        def __init__(self, name: str, age: int, float: float, bool: bool, list: list, dict: dict):
            self.name = name
            self.age = age
            self.float = float
            self.bool = bool
            self.list = list
            self.dict = dict

    p = Person("kainhuck", 18, 18.8, True, ["1", 1], {"a": "!!!!!"})

    print(marshal(p))


# 类的属性包含其他类
def test2():
    class B(object):
        def __init__(self, bb: str):
            self.bb = bb

    class A(object):
        def __init__(self, name: str, b: B):
            self.name = name
            self.b = b

    a = A("kainhuck", B("asdasd"))
    print(marshal(a))


if __name__ == '__main__':
    test1()
    test2()
