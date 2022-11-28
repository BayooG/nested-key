
def getNestedKeyValue(obj: dict, keys: list):
    if len(keys) == 1:
        return obj.get(keys[0], None)
    else:
        return getNestedKeyValue(obj.get(keys[0], {}), keys[1:])