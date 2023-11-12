"""
Initial run point for proj, parse required arguments in file and out file
Modified to use recursive functions for Lab 2

__author__ = Alex Shah
__version__ = proj2
"""

from pathlib import Path
import argparse
from proj.proj1 import process_files  # Import process_files from proj module version proj
from proj.proj2 import recursive_process_files # Import recursive_process_files from proj module version proj2


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
    arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
    args = arg_parser.parse_args()

    in_file_path = args.in_file
    out_file_path = args.out_file

    in_path = Path(in_file_path)
    out_path = Path(out_file_path)

    with in_path.open('r') as input_file, out_path.open('w') as output_file:
        recursive_process_files(input_file, output_file)


if __name__ == "__main__":
    main()
