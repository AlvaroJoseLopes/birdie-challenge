def delete_transformation(data: dict, key: str) -> dict:
    """
    Deletes the key from the dictionary

        Parameters:
            data (dict): target dictionary
            key (str): key to be deleted

        Returns:
            data (dict): target dictionary after applying `deletion` transformation.
    """
    data.pop(key, None)
    return data


def set_transformation(data: dict, key: str, value: str) -> dict:
    """
    Sets the value for a key in the dictionary

        Parameters:
            data (dict): target dictionary
            key (str): target key
            value (str): value to store

        Returns:
            data (dict): target dictionary after applying `set` tranformation.
    """
    data[key] = value
    return data


def rename_transformation(data: dict, old_key: str, new_key: str) -> dict:
    """
    Renames the `old_key`to `new_key` in the dictionary

        Parameters:
            data (dict): target dictionary
            old_key (str): previous key to be renamed
            new_key (str): renamed key

        Returns:
            data (dict): target dictionary after applying `rename` tranformation.
    """
    current_value = data.get(old_key, None)
    if current_value is not None:
        data = set_transformation(data, new_key, current_value)

    data = delete_transformation(data, old_key)

    return data
