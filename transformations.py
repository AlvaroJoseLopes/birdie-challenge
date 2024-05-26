def delete_transformation(data: dict, key1: str) -> dict:
    """
    Deletes the key from the dictionary

        Parameters:
            data (dict): target dictionary
            key1 (str): key to be deleted

        Returns:
            data (dict): target dictionary after applying `deletion` transformation.
    """
    data.pop(key1, None)
    return data


def set_transformation(data: dict, key1: str, value1: str) -> dict:
    """
    Sets the value for a key in the dictionary

        Parameters:
            data (dict): target dictionary
            key1 (str): target key
            value1 (str): value to store

        Returns:
            data (dict): target dictionary after applying `set` tranformation.
    """
    data[key1] = value1
    return data


def rename_transformation(data: dict, key1: str, key2: str) -> dict:
    """
    Renames the `old_key`to `new_key` in the dictionary

        Parameters:
            data (dict): target dictionary
            key1 (str): previous key to be renamed
            key2 (str): renamed key

        Returns:
            data (dict): target dictionary after applying `rename` tranformation.
    """
    current_value = data.get(key1, None)
    if current_value is not None:
        data = set_transformation(data, key2, current_value)
        data = delete_transformation(data, key1)

    return data
