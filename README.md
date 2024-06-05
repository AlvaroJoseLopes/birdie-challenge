# Birdie.ai challenge

My solution for the birdie.ai challenge (SWE intern position)
For more details about the challenge check the [description](challenge.md).

## Solution

The solution was made in Python 3.10.14.

For this solution, the following steps were followed:
1. JSON deserialization
2. Parsing of each provided transformation type and arguments 
3. Apply each transformation on the object
4. JSON serialization of the transformed content

### Step 1.
For the JSON deserialization the following scenarios were considered:
- All the content fits memory
- The content doesn't fit in memory 

To accomplish both scenarios the deserialization was made in chunks (with a max size in bytes specified by the user, for default 8MB - cost-throughput optimal for OLAP [1] ). 

The generator function responsible for that was `json_reader.read_json()` which reads a JSON file in chunks and yields each chunk as a dictionary.

### Step 2.
Since the transformations follow the pattern: `{transformation_type}:{parameter1}:{parameter2}:...` we can easily parse each argument and extract the type of the transformation and its parameters.

The method responsible for that is `transformation_parser.parse()` and returns a tuple where the first element is a string indicating the transformation type (e.g., "delete", "set", "rename") and the second element is a dictionary with the corresponding keyword parameters.
For example:
- `delete:color` returns `("delete", {"key": "color"})`

### Step 3.
After parsing each transformation and its parameter we can apply the transformation to the chunks.

The file `transformations.py` contains one method for each transformation and takes as an argument the deserialized content (`dict`) and its parameters and returns the content after applying the transformation.

**Note:** There is no need to have the entire JSON content in memory to apply the transformations.

### Step 4.
The final step is to serialize the transformed content into another file. 

To accomplish that the class `json_writer.JsonWriter` that dumps the content into .json (in chunks) was implemented. The method `write()` takes a chunk and writes it into the file. This class when used as context manager also ensures that the final file - with appended chunks - is a valid JSON file.

## How to use it

```
usage: transform.py [-h] [-t TRANSFORMATIONS [TRANSFORMATIONS ...]] -i INPUT_FILE -o OUTPUT_FILE [-cs CHUNKSIZE]

A command-line program that performs transformations on the input JSON

options:
  -h, --help            show this help message and exit
  -t TRANSFORMATIONS [TRANSFORMATIONS ...], --transformations TRANSFORMATIONS [TRANSFORMATIONS ...]
                        List of transformations
  -i INPUT_FILE, --input_file INPUT_FILE
                        .json input file
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        .json output file
  -cs CHUNKSIZE, --chunksize CHUNKSIZE
                        Max chunksize
```
Example:
```bash
python3 transform.py -t delete:color set:number:three rename:pet:animal
```

## References
[1] Dominik Durner, Viktor Leis, and Thomas Neumann. 2023. Exploiting Cloud Object Storage for High-Performance Analytics. Proc. VLDB Endow. 16, 11 (July 2023), 2769–2782. https://doi.org/10.14778/3611479.3611486
