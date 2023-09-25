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
            output_file.write(ans + '\n')
        except ValueError as e:
            # Handle invalid expressions
            print(f'Error: {e}', file=stderr)


#  Check operator
def isOperator(c: str) -> bool:
    if c in ['+', '_', '*', '/', '^', '$']:
        return True
    else:
        return False


def convert_prefix_to_postfix(pre: str) -> str:
    s = MyStack()

    # reverse input string
    pre = pre[::-1]

    for i in pre:
        if isOperator(i):
            a = s.pop()
            b = s.pop()
            s.push(str(a + b + i))
        else:
            s.push(i)
    ss = []
    while not s.is_empty():
        ss += s.pop()
        return str(*ss)
