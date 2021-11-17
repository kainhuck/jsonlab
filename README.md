# jsonlab

![GitHub](https://img.shields.io/github/license/kainhuck/jsonlab?style=flat-square) ![PyPI](https://img.shields.io/pypi/v/jsonlab?style=flat-square) ![PyPI - Format](https://img.shields.io/pypi/format/jsonlab?style=flat-square) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jsonlab?style=flat-square) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/jsonlab?style=flat-square) ![PyPI - Downloads](https://img.shields.io/pypi/dm/jsonlab?style=flat-square)

## 介绍

众所周知，python内置的json不提供将json字符串序列化成json字符串(`__dict__`可序列化一层字典，不能递归)
，也不提供将json字符串反向序列化成类对象的功能，为了解决这个痛点，再多方寻找无果后，决心自己开发提供该功能的库，现已开发完毕，在此公布于大众，以造福全人类。

## 安装

> pip3 install jsonlab

## 使用场景

该库适用于对自定义类型的json序列化和json反序列化，比如我们在网络通信时定义了自己的模型，我们便可通过该库来将自定义类型实例序列化成json字符串发送，或者将接收到得json字符串反序列化成类实例。

## 注意

由于json序列化和反序列化时我们需要知道对象的类型，然而python语言的弱类型特征不能直观的获取属性类型，所以在使用这个库时有个约定：

````
1. 自定义的类型必须实现 __init__ 方法，且 __init__ 方法中必须包含所有要序列化反序列化的属性，并且，这些属性必须作为形参出现在 __init__ 方法的形参列表中，并且需要有对应的类型注解

2. 序列化/反序列化时是以 __init__ 函数中形参名作为key值，所以为了防止不必要的bug，请保持形参名和属性名一致
````

**例1：**

下面的`Person`类是一个典型的满足需求的定义

```python
class Person(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# or

class Person(object):
    def __init__(self, name: str = "kainhuck", age: int = 18):
        self.name = name
        self.age = age
```

**例2：**

下面的`Person`类中`hobby`属性将不会被序列化或反序列化

```python
class Person(object):
    def __init__(self, name: str, age: int, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby


# or

class Person(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.hobby = ""
```

**例3：**

下面例子演示了继承类的写法

```python
class B(object):
    def __init__(self, b_name: str):
        self.b_name = b_name


class A(B):
    def __init__(self, a_name: str, b_name: str):
        super().__init__(b_name)
        self.a_name = a_name
```

**例4：**

下面的例子演示了属性是其他类型的情况

```python
class B(object):
    def __init__(self, b_name: str):
        self.b_name = b_name


class A(object):
    def __init__(self, a_name: str, b: B):
        self.a_name = a_name
        self.b = b
```

**例5：**

下面的例子演示了列表的使用, 需要注意的是:

1. 如果一个类的属性是个列表，则可以使用 `list` 或者 `[子类型]`

2. 如果采用第二种写法，目前只支持一种类型，也就`len([子类型]) == 1`

3. 子类型支持一下几种情况

   | 子类型名         | 描述                                                         |
      | ---------------- | ------------------------------------------------------------ |
   | str              | 内置类型 -- 字符串                                           |
   | int              | 内置类型 -- 整数                                             |
   | float            | 内置类型 -- 浮点数                                           |
   | bool             | 内置类型 -- 布尔                                             |
   | list             | 内置类型 -- 普通列表(内部不可为自定义类型)                   |
   | dict             | 内置类型 -- 普通字典(内部不可为自定义类型)                   |
   | object           | 表示支持任意类型（但是不支持自定义类型） [object] == list    |
   | 自定义类型       | 自定义类型，目前只支持一个，也就是说一个list内部只有一种自定义类型 |
   | [子类型]         | 嵌套list                                                     |
   | {key类型:子类型} | 嵌套字典                                                     |

```python
class A:
    def __init__(self, values: [str]):
        self.values = values


# or 

class B:
    def __init__(self, b_name: str):
        self.b_name = b_name


class A:
    def __init__(self, values: [B]):
        self.values = values


# or

class A:
    def __init__(self, values: [[str]]):
        self.values = values


# or

class A:
    def __init__(self, values: [{str: object}]):
        self.values = values
```

**例6：**

下面的例子演示了字典的使用，需要注意的是：

1. 如果一个类的属性是个字典，则可以使用 `dict` 或者 `{key类型:value类型}`

2. 如果采用第二种写法，目前只支持一种类型，也就`len({key类型:value类型}) == 1`

3. key类型支持如下

    1. str
    2. int
    3. float
    4. bool

4. value类型支持如下

   | 类型名           | 描述                                                         |
      | ---------------- | ------------------------------------------------------------ |
   | str              | 内置类型 -- 字符串                                           |
   | int              | 内置类型 -- 整数                                             |
   | float            | 内置类型 -- 浮点数                                           |
   | bool             | 内置类型 -- 布尔                                             |
   | list             | 内置类型 -- 普通列表(内部不可为自定义类型)                   |
   | dict             | 内置类型 -- 普通字典(内部不可为自定义类型)                   |
   | object           | 表示支持任意类型（但是不支持自定义类型） [object] == list    |
   | 自定义类型       | 自定义类型，目前只支持一个，也就是说一个list内部只有一种自定义类型 |
   | [子类型]         | 嵌套list                                                     |
   | {key类型:子类型} | 嵌套字典                                                     |

```python
class A:
    def __init__(self, values: {str: str}):
        self.values = values


# or 

class B:
    def __init__(self, b_name: str):
        self.b_name = b_name


class A:
    def __init__(self, values: {str: B}):
        self.values = values


# or

class A:
    def __init__(self, values: {str: [str]}):
        self.values = values


# or

class A:
    def __init__(self, values: {str: {str: object}}):
        self.values = values
```

## Usage

**接口**

- `marshal(obj) -> str`

  传递一个类实例，返回一个序列化后的json字符串

- `marshal_to_dict(obj) -> dict`

  传递一个类实例，返回一个字典对象

- `unmarshal(json_, type_: type)`

  第一个参数可以是: json字符串，bytes类型的json字符串，字典对象

  第二个参数是自定义类型

  返回自定义类型的实例

**demo**

- 序列化: [demo](example/marshal_demo.py)
- 反序列化: [demo](example/unmarshal_demo.py)
