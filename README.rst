jsonparser
=======
这个库可以将json字符串解析成类对象

-----------------------------

todo

1. 发布到pypi

-----------------------------

Usage
>>>>>

python::

  import jsonparser

  class Person(object):
      def __init__(self, name:str, age:int):
          self.name = name
          self.age = age

  json_str = '{"name":"kainhuck", "age":12}'

  p = jsonparser.json_to_obj(json_str, Person)
  assert isinstance(p, Person)
  ...


