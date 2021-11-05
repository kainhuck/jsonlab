from jsonparser import json_to_obj


def test1():
    class B:
        def __init__(self, bbb: str):
            self.bbb = bbb

    class A:
        def __init__(self, name: str, b: B, dict: dict):
            self.name = name
            self.b = b
            self.dict = dict

    js1 = '{"name":"kainhuck", "b":{"bbb":"bbb"}, "dict":{"a":1, "b":"b"}}'
    js2 = '{"b":{"bbb":"bbb"}, "dict":{"a":1, "b":"b"}}'
    a = json_to_obj(js1, A)
    print(a.name)
    print(a.b)
    print(a.b.bbb)
    print(a.dict)


def test2():
    class A(object):
        def __init__(self, names: [str]):
            self.names = names

    js = '{"names":["sdf","dasd"]}'
    a = json_to_obj(js, A)
    print(a.names)


def test3():
    class A(object):
        def __init__(self, names: [dict]):
            self.names = names

    js = '{"names":[{"a":1},{"b":"a"}]}'
    a = json_to_obj(js, A)
    print(a.names)


def test4():
    class B(object):
        def __init__(self, h: str):
            self.h = h

    class A(object):
        def __init__(self, names: [B]):
            self.names = names

    js = '{"names":[{"h":1},{"h":"a"}]}'
    a = json_to_obj(js, A)
    print(a.names)
    print(a.names[0].h)


def test5():
    class B(object):
        def __init__(self, h: str):
            self.h = h

    class A(object):
        def __init__(self, names: {str: B}):
            self.names = names

    js = '{"names":{"a":{"h":1}, "b":{"h":2}}}'
    a = json_to_obj(js, A)
    print(a.names)
    print(a.names["a"].h)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
