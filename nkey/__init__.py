class ND:
    @staticmethod
    def nkey(obj: dict, key: str, sep: str = "."):
        """keys a nested value in dict

        Args:
            obj (dict): dict
            key (str): the keys in a string format separated by the separator.
            sep (str, optional): the separator. Defaults to ".".

        Returns:
            value: returns the value of the nested key if it exists.
        """
        keys = key.split(sep)
        return ND.get_value(obj, keys)

    @staticmethod
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
            return ND.get_value(obj.get(keys[0], {}), keys[1:])
