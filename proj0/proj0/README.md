# Proj 0

This is an analog to the Java Proj0 posted on the blackboard site. It is far from perfect is meant to be representative
of a 'B' level submission.

This document is written in [Markdown](https://dillinger.io/). Use the link to render if needed. Most IDEs render 
markdown, and it is currently a de facto standard in modern day software documentation.

This project also includes a guide on formatting python projects as a package.

## Running Proj 0

> NOTE: Your IDE may configure the project implicitly as a module. 
> **BE SURE TO RUN STEP 4 BEFORE SUBMITTING LABS** 

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m proj0 -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m proj0 <some_input_file> <some_output_file>`
   a. IE: `python -m proj0 resources/input/in.txt output.txt`

Output will be written to the specified output file after processing the input file.

### Proj 0 Usage:

```commandline
usage: python -m proj0 [-h] in_file out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  -h, --help  show this help message and exit
```

Usage statements are very formalized

| Symbol        | Meaning                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| [var]         | variable var is optional.                                                                                          |
| var           | variable var is required. All positional arguments are required.                                                   |
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values                                                                            |
| *             | This argument consumes 0 or more values                                                                            |

## Sample Python Packaging

To make code more portable, you need to package (especially in the real world) python modules. This is just a special
directory layout with a few optional files.

### Project Layout

Packages are groups of modules that work together to act as a library or program. Having a single module in a package is
fine, but you can (and plenty of times should) have more. Each module is made up of related python script(s). Here is our
605.202.proj0 example package explained.

* [proj0/](.): The parent or "root" folder containing all of these files. Can technically have any name.
    * [README.md](README.md):
      The guide you're reading. All software should come with a readme!
    * [proj0](proj0): 
      This is a *module* in our *package*. Be sure to name it appropriately
      * [`__init__.py`](proj0/__init__.py) 
        This is a very important file and is often blank. It is used to expose what functions, variables, classes, etc are exposed when scripts import this module. See the example file. It can also hide functions/variables
      * [`__main__.py`](proj0/__main__.py) 
        This file is the entrypoint to your program when ran as a program. It usually just handles command line arguments, similar to Java and C's main() functions.
      * `*.py` 
        These are python scripts that do the actual work.

### Python Packages

So why all this fuss?

Python files can be relatively imported (ie import ../../../someones_code), however A LOT of things can/will break.
This is not a portable way to structure your code. This is especially true if a file that is relatively imported 
attempts to perform a relative import. All relativity is based at the directory that python is *invoked* and **NOT** on
the directory that contains the python file.

If you shared a single python file, the recipient would only be able to run what you wrote. If they wanted to 
incorporate your algorithms into their project they would need to make a module themselves, cut and paste the relevant
chunks of your code, or deal with issues from above.

#### Distribution

> Note this section is not required, but instead for informational purposes

This file structure could further be packaged into an installable package (with a few extra undocumented steps) and then 
could be used as us such:

```python
from pathlib import Path
# Reminder, to import this way, there are more undocumented steps that require installing proj0 to the system libraries
import proj0

# open input file as read, output file as write
with Path('input.txt').open('r') as my_input_file, Path('output.txt').open('w') as my_output_file:
    proj0.process_files(my_input_file, my_output_file)
```

Additionally, this allows the end user to run your code from any directory, so long as they run it as a module. This is
done with the previously demonstrated m flag to python: `python -m <module>`.

```bash
# assuming proj0 has been installed to the python environment (Not documented here)
python -m proj0 input.txt output.txt
```

## What To Submit

Create a package for each lab. IE username_lab1.

Inside that package, include your modules with python code and a Readme.

Zip your package.

Avoid including:
* IDE setting files (ie .idea/ .vscode/ .eclipse/ etc)
* Python cache files (*.pyc or __pycache__/)
* Any binary data
* Extraneous logs
* Python environments (ie .venv/ .env/)
* etc
