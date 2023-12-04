"""
Initial run point for proj, requires no args for proj4

__author__ = Alex Shah
__version__ = proj4
"""
from pathlib import Path
import argparse
from proj.tests import run_sorts


def main():
    arg_parser = argparse.ArgumentParser()
    args = arg_parser.parse_args()

    run_sorts()


if __name__ == "__main__":
    main()
