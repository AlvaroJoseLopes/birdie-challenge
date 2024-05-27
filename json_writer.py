import json


class JsonWriter:
    """
    File Writer that dumps the content .json content in chunks
    """

    def __init__(self, filepath: str):
        """
        Initializes the JsonWriter with the given file path.

        Parameters:
            filepath (str): The path of the file to write JSON content to.
        """
        self.fp = open(filepath, "w")

    def close(self):
        """
        Closes the file after ensuring proper JSON formatting.
        """
        # Removing final ',' and closing object
        self.fp.seek(self.fp.tell() - 1)
        self.fp.write("\n}")
        self.fp.close()

    def write(self, chunk_content: dict):
        """
        Writes a chunk of content to the JSON file.

        Parameters:
            chunk_content (dict): The dictionary content to write as a JSON chunk.
        """
        dumped_content = json.dumps(chunk_content, indent=2)
        # Removing { and \n} from the dumped content
        dumped_content = dumped_content[1:-2] + ","
        self.fp.write(dumped_content)

    def __enter__(self):
        """
        Enters the runtime context related to this Json Writer.

        This method initializes the JSON object structure by writing the opening
        curly brace to the file.
        """
        # opening JSON object
        self.fp.write("{")
        return self

    def __exit__(self, *args):
        """
        Exits the runtime context related to this object.

        Parameters:
            *args: Additional arguments (unused in this context).
        """
        self.close()
