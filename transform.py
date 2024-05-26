import argparse
from transformations import *
from transformation_parser import parse
from json_reader import read_json
from json_writer import JsonWriter


def main(args):
    with JsonWriter(args.output_file) as fp_out:
        for idx, data in enumerate(read_json(args.input_file)):
            print(f"Processing chunk {idx+1}")
            for transformation in args.transformations:
                transformation_type, t_args = parse(transformation)
                match transformation_type:
                    case "delete":
                        data = delete_transformation(data, **t_args)
                    case "set":
                        data = set_transformation(data, **t_args)
                    case "rename":
                        data = rename_transformation(data, **t_args)
                    case _:
                        raise NotImplementedError(
                            f"{transformation_type} transformation was not implemented."
                        )
            fp_out.write(data)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        description="Command-line program that performs transformations on the input json"
    )
    argparser.add_argument(
        "-t", "--transformations", nargs="+", help="List of transformations", default=[]
    )
    argparser.add_argument(
        "-i",
        "--input_file",
        help=".json input file",
        required=True,
        default="data/input.json",
    )
    argparser.add_argument(
        "-o",
        "--output_file",
        help=".json output file",
        required=True,
        default="data/output.json",
    )
    argparser.add_argument(
        "-cs",
        "--chunksize",
        help="Max chunksize",
        required=False,
        default=8 * 2**20,  # 8MB
    )
    args = argparser.parse_args()
    main(args)
