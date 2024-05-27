import json
import sys
from typing import Generator


def pre_process_chunk(chunk: str) -> dict:
    """
    Pre-processes a chunk of JSON data and deserialize content.

    Parameters:
        chunk (str): A string containing JSON data.

    Returns:
        dict: The deserialized JSON data as a dictionary.
    """
    if chunk.endswith(","):
        chunk = chunk[:-1]
    if not chunk.startswith("{"):
        chunk = "{" + chunk
    if not chunk.endswith("}"):
        chunk += "}"
    content = json.loads(chunk)
    return content


def read_json(
    file_path: str, max_chunksize: int = 8 * 2**20
) -> Generator[dict, None, None]:
    """
    Generator function that reads a .json file content in chunks with a maximum size.

    This function reads a JSON file in chunks and yields each chunk as a dictionary.
    It ensures efficient memory usage when dealing with large JSON files.

    Parameters:
        file_path (str): The path to the target .json file.
        max_chunksize (int): The maximum size for each chunk in bytes. Default is 8MB.

    Yields:
        dict: The deserialized content of each chunk as a dictionary.
    """
    with open(file_path, "r") as f:
        chunk = ""
        for x in f.readlines():
            x = x.rstrip()
            chunk += x
            current_size = sys.getsizeof(chunk)
            if current_size > max_chunksize:
                content = pre_process_chunk(chunk)
                yield content
                chunk = ""

    # Last chunk
    if len(chunk) > 0:
        yield pre_process_chunk(chunk)
