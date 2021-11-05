import json

BASE_TYPES = (str, int, float, list, tuple, dict)
KEY_TYPES = (str, int, float, tuple)


# 把 value 转换成 type_ 类型
def to_arg(type_, value):
    if type_ in BASE_TYPES:  # 如果是普通类型
        if value is None:
            return type_()
        return type_(value)
    else:
        if isinstance(type_, type):  # 自定义类型
            return json_to_obj(value, type_)
        else:
            if isinstance(type_, list):  # [type] 比如 type_ = [str]
                if value is None:
                    return None
                assert isinstance(value, list)
                assert len(type_) == 1
                sub_type = type_[0]
                assert isinstance(sub_type, type)

                # 将 value 中每个值转换成 sub_type 类型
                list_values = []
                if sub_type in BASE_TYPES:  # 基础类型
                    for v in value:
                        if v is None:
                            list_values.append(None)
                        else:
                            list_values.append(sub_type(v))
                elif sub_type is object:
                    for v in value:
                        list_values.append(v)
                else:  # 自定义类型, 这种情况 value 应该是一个 dict
                    for v in value:
                        list_values.append(json_to_obj(v, sub_type))
                return list_values
            elif isinstance(type_, dict):  # {type:type} | 第一个type必须是 KEY_TYPES 中的类型
                if value is None:
                    return None
                assert isinstance(value, dict)
                assert len(type_) == 1
                key_type = list(type_.keys())[0]
                assert key_type in KEY_TYPES
                value_type = list(type_.values())[0]
                dict_value = {}
                if value_type in BASE_TYPES:
                    for k, v in value.items():
                        if v is None:
                            dict_value[key_type(k)] = None
                        else:
                            dict_value[key_type(k)] = value_type(v)
                elif value_type is object:
                    for k, v in value.items():
                        dict_value[key_type(k)] = v
                else:  # 自定义类型
                    for k, v in value.items():
                        dict_value[key_type(k)] = json_to_obj(v, value_type)
                return dict_value


# json 可以是str或者dict
def json_to_obj(json_, type_: type):
    if json_ is None:
        return None

    # 1. 判断所给的类型是否包含 __init__ 方法
    if not hasattr(type_.__init__, "__annotations__"):
        raise Exception(f"{type_} need `__init__` method")

    init_func_annotations = type_.__init__.__annotations__

    # 2. 将 json_str 转化成字典对象
    if isinstance(json_, str):
        json_dict = json.loads(json_)
    elif isinstance(json_, dict):
        json_dict = json_
    else:
        raise Exception("only support `str` or `dict` type for `json_`")

    # 3. 获取所给的类型包含的属性以及类型
    args = []
    for k, v in init_func_annotations.items():
        args.append(to_arg(v, json_dict.get(k)))

    return type_(*tuple(args))
