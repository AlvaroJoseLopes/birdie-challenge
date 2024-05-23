import json


def parse_transformation_arg(arg) -> tuple[str, dict[str, str]]:
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
                - ("delete", {"key": "color"})
                - ("set", {"key": "number", "value": "three"})
                - ("rename", {"old_key": "first_name", "new_key": "last_name"})
    """
    tokens = arg.split(":")

    if tokens[0] == "delete" and len(tokens) == 2:
        return "delete", {"key": tokens[1]}
    elif tokens[0] == "set" and len(tokens) == 3:
        return "set", {"key": tokens[1], "value": tokens[2]}
    elif tokens[0] == "rename" and len(tokens) == 3:
        return "rename", {"old_key": tokens[1], "new_key": tokens[2]}
    else:
        raise ValueError(f"Invalid transformation: {arg}")


def read_json(file_path: str) -> dict:
    """
    Reads .json file content

        Parameters:
            file_path (str): target .json file path

        Returns:
            content (dict): deserialized content from the file stored as dictionary
    """
    content = None
    with open(file_path, "r") as f:
        content = json.load(f)

    return content


def save_file(data: dict, output_path: str):
    """
    Dumps content on data into a .json file specified

        Parameters:
            data (dict): dictionary with the content
            output_path (str): target .json file path
    """
    content = json.dumps(data, indent=2)
    with open(output_path, "w") as f:
        f.write(content)
