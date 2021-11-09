# jsonparser

这个库可以将json字符串解析成类对象，可满足日常百分之90+的情况

-----------------------------

## Usage

```python
import jsonparser

class Person(object):
  def __init__(self, name:str, age:int):
      self.name = name
      self.age = age

json_str = '{"name":"kainhuck", "age":12}'

p = jsonparser.parse(json_str, Person)
assert isinstance(p, Person)
...
```

更多例子见: [demo](example/demo.py)


## todo

1. 发布到pypi