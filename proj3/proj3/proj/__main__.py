"""
Initial run point for proj, parse required arguments for the frequency table,
input/output files, and mode to encode or decode.
Modified for huffman coding for Lab 3

__author__ = Alex Shah
__version__ = proj3
"""
from pathlib import Path
import argparse
from proj.proj3 import huffman_process_files


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("mode", choices=['encode', 'decode'], help="Operation mode: encode or decode")
    arg_parser.add_argument("frequency_table", type=str, help="Frequency Table Pathname")
    arg_parser.add_argument("input_file", type=str, help="Input File Pathname")
    arg_parser.add_argument("output_file", type=str, help="Output File Pathname")
    args = arg_parser.parse_args()

    mode = args.mode
    frequency_table_path = args.frequency_table
    input_file_path = args.input_file
    output_file_path = args.output_file

    freq_path = Path(frequency_table_path)
    input_path = Path(input_file_path)
    output_path = Path(output_file_path)

    with freq_path.open('r') as freq_file, input_path.open('r') as input_file, output_path.open('w') as output_file:
        huffman_process_files(freq_file, input_file, output_file, mode)


if __name__ == "__main__":
    main()