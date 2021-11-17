import json

import jsonlab


# 属性是自定义类型，属性是字典类型，属性是基础类型
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
    a = jsonlab.unmarshal(js1, A)
    print(a.name)
    print(a.b)
    print(a.b.bbb)
    print(a.dict)


# 属性是指定类型的列表，注意目前只支持列表中唯一类型，或则 使用 list（这种是普通列表，不会将内部的字典序列化成对象）
def test2():
    class A(object):
        def __init__(self, names: [str]):
            self.names = names

    js = '{"names":["sdf","dasd"]}'
    a = jsonlab.unmarshal(js, A)
    print(a.names)


# 属性是字典类型的列表
def test3():
    class A(object):
        def __init__(self, names: [dict]):
            self.names = names

    js = '{"names":[{"a":1},{"b":"a"}]}'
    a = jsonlab.unmarshal(js, A)
    print(a.names)


# 属性是自定义类型的列表
def test4():
    class B(object):
        def __init__(self, h: str):
            self.h = h

    class A(object):
        def __init__(self, names: [B]):
            self.names = names

    js = '{"names":[{"h":1},{"h":"a"}]}'
    a = jsonlab.unmarshal(js, A)
    print(a.names)
    print(a.names[0].h)


# 属性是指定key，value类型的字典，value；类型为自定义类型
def test5():
    class B(object):
        def __init__(self, h: str):
            self.h = h

    class A(object):
        def __init__(self, names: {str: B}):
            self.names = names

    js = '{"names":{"a":{"h":1}, "b":{"h":2}}}'
    a = jsonlab.unmarshal(js, A)
    print(a.names)
    print(a.names["a"].h)


# 类继承例子
def test6():
    class Base(object):
        def __init__(self, name: str):
            self.name = name

    class Person(Base):
        def __init__(self, name: str, age: int):
            super().__init__(name)
            self.age = age

    js = '{"name":"kainhuck", "age":18}'
    p = jsonlab.unmarshal(js, Person)
    assert isinstance(p, Person)
    print(p.name)
    print(p.age)


# 类属性是任意类型列表例子, 同 list
def test7():
    class Person(object):
        def __init__(self, any: [object]):  # == def __init__(self, any: list)
            self.any = any

    js = '{"any": ["string", 18, {"a":"a"}, [1,2,"3"]]}'

    p = jsonlab.unmarshal(js, Person)
    print(p.any)


# 类属性是字典，其中 key 为指定类型，value为任意类型
def test8():
    class Person(object):
        def __init__(self, things: {str: object}):
            self.things = things

    js = '''{
              "things": {
                         "a":{"name":"a"}, 
                         "b":["b", 1],
                         "c":1,
                         "d":false
                         }
             }'''

    p = jsonlab.unmarshal(js, Person)
    assert isinstance(p, Person)
    print(p.things)
    print(p.things["a"])
    print(p.things["b"])
    print(p.things["c"])
    print(p.things["d"])


# 二进制json字符串也支持
def test9():
    class Person(object):
        def __init__(self, any: [object]):  # == def __init__(self, any: list)
            self.any = any

    js = b'{"any": ["string", 18, {"a":"a"}, [1,2,"3"]]}'
    p = jsonlab.unmarshal(js, Person)
    print(p.any)


# 类的属性是嵌套列表
def test10():
    class B(object):
        def __init__(self, name: str):
            self.name = name

    class A(object):
        def __init__(self, value: [[B]]):
            self.value = value

    js = '''{
              "value": [
                [{"name":"a1"},{"name":"a2"},{"name":"a3"}],
                [{"name":"b1"},{"name":"b2"},{"name":"b3"}],
                [{"name":"c1"},{"name":"c2"},{"name":"c3"}]
              ]
            }'''
    a = jsonlab.unmarshal(js, A)
    print(a.value[0][0].name)


# 类的属性是列表嵌套字典
def test11():
    class B(object):
        def __init__(self, name: str):
            self.name = name

    class A(object):
        def __init__(self, value: [{str: B}]):
            self.value = value

    js = '''
        {
            "value": [
              {"a": {"name":"a"}},
              {"b": {"name":"b"}},
              {"c": {"name":"c"}}
            ]
        }
    '''
    a = jsonlab.unmarshal(js, A)
    print(a.value[1]["b"].name)


# 类的属性是字典嵌套字典嵌套列表
def test12():
    class A:
        def __init__(self, values: {str: {str: [object]}}):
            self.values = values

    js = '''
    {
        "values":{
            "a":{
                "a1": [1, 2, "3", 3.14]
            },
            "b":{
                "b1": [1, 2, "3", 3.14]
            }
        }
    }
    '''
    a = jsonlab.unmarshal(js, A)
    print(a.values)
    print(a.values["a"]["a1"])


# 类的属性是字符串，但实际上是字典/列表
def test13():
    class A:
        def __init__(self, dict_data: str, list_data: str):
            self.dict_data = dict_data
            self.list_data = list_data

    js = '''
    {
      "dict_data": {"name":"kainhuck", "value":true},
      "list_data": [1, "a", true]
    }
    '''

    a = jsonlab.unmarshal(js, A)
    print(a.dict_data)
    print(a.list_data)
    json.loads(a.dict_data)
    json.loads(a.list_data)


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
    test12()
    test13()
