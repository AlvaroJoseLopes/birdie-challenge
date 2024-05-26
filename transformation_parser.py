def parse(arg) -> tuple[str, dict[str, str]]:
    """
    Parses the transformation args

        Parameters:
            arg (str): transformation argument, e.g delete:color or set:number:three
                       Pattern: {transformation_type}:{parameter1}:{parameter2}
        Returns:
            tuple: A tuple where the first element is a string indicating the transformation type
               (e.g., "delete", "set", "rename") and the second element is a dictionary with
               the corresponding parameters.
            For example:
                - ("delete", {"key1": "color"})
                - ("set", {"key1": "number", "val1": "three"})
                - ("rename", {"key1": "first_name", "key2": "last_name"})
    """
    tokens = arg.split(":")

    if tokens[0] == "delete" and len(tokens) == 2:
        return "delete", {"key1": tokens[1]}
    elif tokens[0] == "set" and len(tokens) == 3:
        return "set", {"key1": tokens[1], "value1": tokens[2]}
    elif tokens[0] == "rename" and len(tokens) == 3:
        return "rename", {"key1": tokens[1], "key2": tokens[2]}
    else:
        raise ValueError(f"Invalid transformation: {arg}")
