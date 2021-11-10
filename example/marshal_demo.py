from jsonlab import marshal


# 类的属性是 基本类型
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


# 类的属性是 自定义类型
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


# 类继承
def test3():
    class B:
        def __init__(self, b_name: str):
            self.b_name = b_name

    class A(B):
        def __init__(self, a_name: str, b_name: str):
            super().__init__(b_name)
            self.a_name = a_name

    a = A("a", "b")
    print(marshal(a))


# 类的属性是 [基本类型]
def test4():
    class A:
        def __init__(self, values: [str]):
            self.values = values

    a = A(["1", "b"])
    print(marshal(a))


# 类的属性是 [自定义类型]
def test5():
    class B:
        def __init__(self, b_name: str):
            self.b_name = b_name

    class A:
        def __init__(self, values: [B]):
            self.values = values

    a = A([B("asdasd"), B("fdsasaS")])
    print(marshal(a))


# 类的属性是 [[...]]
def test6():
    class A:
        def __init__(self, values: [[object]]):
            self.values = values

    a = A([["a", 1], ["b", 2]])

    print(marshal(a))


# 类的属性是 [{...}]
def test7():
    class A:
        def __init__(self, values: [{str: object}]):
            self.values = values

    a = A([
        {"a": 1},
        {"b": "asdas"},
        {"c": {
            "asd": 12,
            "asdas": [1, 2, 3]
        }}
    ])

    print(marshal(a))


# 类的属性是 {str:基本类型}
def test8():
    class A:
        def __init__(self, values: {str: str}):
            self.values = values

    print(marshal(A({"a": "1", "b": "2"})))


# 类的属性是 {str:自定义类型}
def test9():
    class B:
        def __init__(self, b_name: str):
            self.b_name = b_name

    class A:
        def __init__(self, values: {str: B}):
            self.values = values

    print(marshal(A({"a1": B("b1")})))


# 类的属性是 {str:[...]}
def test10():
    class A:
        def __init__(self, values: {str: list}):
            self.values = values

    print(marshal(A({
        "a": [1, 2, 3, "123"]
    })))


# 类的属性是 {str:{...}}
def test11():
    class A:
        def __init__(self, values: {str: {str: object}}):
            self.values = values

    print(marshal(A({
        "a": {
            "a1": 123,
            "a2": [1, 2, 3, "123"],
            "a3": {
                "1": "1"
            }
        }
    })))


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
