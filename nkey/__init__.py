
def get_value(obj: dict, keys: list):
    """gets a value from nested dict

    Args:
        obj (dict): nested dict
        keys (list): list of nest keys

    Returns:
        _type_: _description_
    """
    if len(keys) == 1:
        return obj.get(keys[0], None)
    else:
        return get_value(obj.get(keys[0], {}), keys[1:])