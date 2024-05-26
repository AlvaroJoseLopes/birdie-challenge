import argparse
from utils import *
from transformations import *


def main(args):
    data = read_json(args.input_file)
    for transformation in args.transformations:
        transformation_type, t_args = parse_transformation_arg(transformation)
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
    save_file(data, args.output_file)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        description="Command-line program that performns transformations on the input json"
    )
    argparser.add_argument(
        "-t", "--transformations", nargs="+", help="List of transformations", default=[]
    )
    argparser.add_argument(
        "-i",
        "--input_file",
        help=".json input file",
        required=True,
        default="input.json",
    )
    argparser.add_argument(
        "-o",
        "--output_file",
        help=".json output file",
        required=True,
        default="output.json",
    )
    args = argparser.parse_args()
    main(args)
