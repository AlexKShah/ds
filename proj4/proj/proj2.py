"""
This program receives lines from an input file,
converts prefix expressions to postfix, now with recursion!
and writes them to an output file, now including errors in the output.

In addition, the program now handles cases where there are too few operators
instead of just checking that valid sub expressions can be formed

__author__ = Alex Shah
__version__ = proj3
"""

from sys import stderr
from typing import TextIO
# from proj.mystack import MyStack


def recursive_process_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    read lines from input_file and write converted value to output_file

    :param input_file:
    :param output_file:
    :return:
    """
    for line in input_file:
        # Remove leading and trailing whitespace from the line
        # not necessary since we discard whitespace in algorithm,
        # but prevents us from getting useless lines
        cleaned_line = line.strip()

        # Check if the cleaned line is empty or contains only whitespace
        if not cleaned_line:
            continue

        try:
            # join line to str
            cleaned_line = ''.join(cleaned_line.split())

            # convert prefix to postfix
            ans, index = recursive_convert_prefix_to_postfix(cleaned_line)

            # If we can get through the expression without considering all characters, there must be too few operators
            if index < len(cleaned_line):
                raise ValueError("Finished with expression and found problem, too few operators: " + cleaned_line)

            # write output
            output_file.write("Prefix: " + cleaned_line + "\n")
            output_file.write("Postfix: ")
            output_file.write(ans)
            output_file.write('\n')

        except Exception as e:
            # Handle invalid expressions
            print(f'Error: {e}', file=stderr)
            output_file.write(f'Error: {e} \n')


def is_operator(c: str) -> bool:
    """
    Check if character is an operator
    :param c:
    :return:
    """
    return c in ['+', '-', '*', '/', '^', '$']


def recursive_convert_prefix_to_postfix(pre: str, index: int = 0) -> (str, int):
    """
    Convert prefix expressions to postfix expressions, now with recursion!
    :param index: integer position in expression
    :param pre: prefix expression string
    :return: postfix expression and current end index
    """
    # If the end of our expression is longer than the expression, we must be missing an operand
    try:
        # consider character at the end of current expression
        char = pre[index]
    except IndexError as e:
        raise IndexError("Could not continue with the expression, too few operands: " + str(pre))

    if is_operator(char):
        try:
            # Recursively find the operands for the operator
            operand1, index = recursive_convert_prefix_to_postfix(pre, index + 1)
            operand2, index = recursive_convert_prefix_to_postfix(pre, index)
        except ValueError as e:
            # If we can't match up operands for the operator, then we have too few operators
            raise ValueError("Problem recursing with the expression, too few operators: " + str(pre))

        # Make a sub expression, recurse back up providing the end index in the tuple
        return operand1 + operand2 + char, index
    else:
        # operand, recurse back up  and try next character
        return char, index + 1
