# jsonparser

这个库可以将json字符串解析成类对象，可满足日常百分之90+的情况

## Usage

- 使用说明

  这个库提供了一个`unmarshal`方法，该方法的第一个参数是`json字符串`或者`二进制json字符串`或者`字典`,第二个参数是要实例化的类型，

  对于该类型，必须满足以下要求：

  1. 包含 `__init__`方法，类的属性必须在该方法中定义
  2. 类的属性参数必须包含在`__init__`方法参数中
  3. `__init__`方法参数必须要有注解
  4. 不满足上述条件之一，则该类（属性）不被序列化（或序列化不成功）
  5. 其他复杂类型属性的定义见[demo](example/unmarshal_demo.py)

- 例子

  ```python
  import jsonparser
  
  class Person(object):
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
  
  json_str = '{"name":"kainhuck", "age":12}'
  
  p = jsonparser.unmarshal(json_str, Person)
  assert isinstance(p, Person)
  ...
  ```

   更多例子见: [demo](example/unmarshal_demo.py)


## todo

2. 发布到pypi