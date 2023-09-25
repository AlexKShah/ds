from sys import stderr
from typing import TextIO
from proj1.mystack import MyStack


def process_files(input_file: TextIO, output_file: TextIO) -> None:
    for line in input_file:
        # Remove leading and trailing whitespace from the line
        cleaned_line = line.strip()

        # Check if the cleaned line is empty or contains only whitespace
        if not cleaned_line:
            continue  # Skip empty or whitespace-only lines

        try:
            # Remove any remaining internal whitespace and convert to postfix
            cleaned_line = ''.join(cleaned_line.split())
            ans = convert_prefix_to_postfix(cleaned_line)
            for an in ans:
                output_file.write(an)
            output_file.write('\n')
        except ValueError as e:
            # Handle invalid expressions
            print(f'Error: {e}', file=stderr)


#  Check operator

def isOperator(c: str) -> bool:
    return c in ['+', '-', '*', '/', '^', '$']


def convert_prefix_to_postfix(pre: str) -> str:
    s = MyStack()
    # Reverse the prefix expression
    reversed_expression = pre[::-1]

    # Iterate through the reversed expression
    for char in reversed_expression:
        if not isOperator(char):
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
                raise ValueError("Not enough operands in the expression: " + str(pre) + " operand1: " + str(operand1) + " operand2: " + str(operand2) + " operator: " + str(char))

    postfix_expression = ""
    while not s.is_empty():
        postfix_expression += s.pop()  # Pop and add items from the stack
    return postfix_expression
