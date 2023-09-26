"""
This program receives lines from an input file,
converts prefix expressions to postfix,
and writes them to an output file.

__author__ = Alex Shah
"""

from sys import stderr
from typing import TextIO
from proj1.mystack import MyStack


def process_files(input_file: TextIO, output_file: TextIO) -> None:
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
            ans = convert_prefix_to_postfix(cleaned_line)

            # write output
            output_file.write("Prefix: " + cleaned_line + "\n")
            output_file.write("Postfix: ")
            output_file.write(ans)
            output_file.write('\n')

        except ValueError as e:
            # Handle invalid expressions
            print(f'Error: {e}', file=stderr)


def is_operator(c: str) -> bool:
    """
    Check if character is an operator
    :param c:
    :return:
    """
    return c in ['+', '-', '*', '/', '^', '$']


def convert_prefix_to_postfix(pre: str) -> str:
    """
    Convert prefix expressions to postfix expressions
    :param pre:
    :return:
    """
    s = MyStack()

    # Reverse the prefix expression
    reversed_expression = pre[::-1]

    # Iterate through the reversed expression
    for char in reversed_expression:
        if char in [" ", "", "\n", "\t"]:
            # discard whitespaces, blanks, tabs, and newlines
            continue
        if not is_operator(char):
            # Operand: Push it onto the stack
            s.push(char)
        else:
            # Operator: Pop two operands from the stack and create a new operand
            operand1 = s.pop()
            operand2 = s.pop()
            if operand1 is not None and operand2 is not None:
                new_operand = operand1 + operand2 + char
                s.push(new_operand)
            else:
                # invalid or incomplete expressions will be reported to console
                raise ValueError("Not enough operands in the expression: " + str(pre) + " operand1: " + str(
                    operand1) + " operand2: " + str(operand2) + " operator: " + str(char))
    postfix_expression = ""
    while not s.is_empty():
        postfix_expression += s.pop()  # Pop and add items from the stack
    return postfix_expression
