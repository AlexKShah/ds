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
    arg_parser.add_argument("frequency_table", type=str, help="Frequency Table Pathname")
    arg_parser.add_argument("encoded_file", type=str, help="Encoded File Pathname")
    arg_parser.add_argument("clear_file", type=str, help="Cleartext File Pathname")
    arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
    args = arg_parser.parse_args()

    frequency_table_path = args.frequency_table
    encoded_file_path = args.encoded_file
    clear_file_path = args.clear_file
    output_file_path = args.out_file

    freq_path = Path(frequency_table_path)
    encoded_path = Path(encoded_file_path)
    clear_path = Path(clear_file_path)
    output_path = Path(output_file_path)

    with freq_path.open('r') as freq_file, encoded_path.open('r') as encoded_file, clear_path.open('r') as clear_file, output_path.open('w') as output_file:
        huffman_process_files(freq_file, encoded_file, clear_file, output_file)


if __name__ == "__main__":
    main()