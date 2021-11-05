import json

BASE_TYPES = (str, int, float, list, tuple, dict)
KEY_TYPES = (str, int, float, tuple)


def to_arg(type_, value):
    if type_ in BASE_TYPES:
        if value is None:
            return type_()
        return type_(value)
    else:
        if isinstance(type_, type):
            return json_to_obj(value, type_)
        else:
            if isinstance(type_, list):
                if value is None:
                    return None
                assert isinstance(value, list)
                assert len(type_) == 1
                sub_type = type_[0]
                assert isinstance(sub_type, type)

                list_values = []
                if sub_type in BASE_TYPES:
                    for v in value:
                        if v is None:
                            list_values.append(None)
                        else:
                            list_values.append(sub_type(v))
                elif sub_type is object:
                    for v in value:
                        list_values.append(v)
                else:
                    for v in value:
                        list_values.append(json_to_obj(v, sub_type))
                return list_values
            elif isinstance(type_, dict):
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
                else:
                    for k, v in value.items():
                        dict_value[key_type(k)] = json_to_obj(v, value_type)
                return dict_value


def json_to_obj(json_, type_: type):
    if json_ is None:
        return None

    if not hasattr(type_.__init__, "__annotations__"):
        raise Exception(f"{type_} need `__init__` method")

    init_func_annotations = type_.__init__.__annotations__

    if isinstance(json_, str):
        json_dict = json.loads(json_)
    elif isinstance(json_, dict):
        json_dict = json_
    else:
        raise Exception("only support `str` or `dict` type for `json_`")

    args = []
    for k, v in init_func_annotations.items():
        args.append(to_arg(v, json_dict.get(k)))

    return type_(*tuple(args))
