"""A collection of useful functions.

The template and this example uses Google style docstrings as described at:
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

"""
from pathlib import Path


def files_to_convert(suffix: str) -> list[Path]:
    """Find files to convert, located below the current working directory.

    Find all files with the given suffix and filter out files from excluded directories.
    Remove files that are not valid for conversion. Valid .py files must contain a
    jupytext heading.

    Args:
        suffix: The  suffix to search for, `py` or `ipynb`

    Returns:
        List of files to be converted.
    """
    root_dir = Path.cwd()
    exclude_dirs = [".nox", ".venv"]

    return [
        file
        for file in root_dir.rglob(f"*.{suffix}")
        if file.is_file()
        and all(excluded not in file.parts for excluded in exclude_dirs)
    ]


def example_function(number1: int, number2: int) -> str:
    """Compare two integers.

    This is merely an example function can be deleted. It is used to show and test generating
    documentation from code, type hinting, testing, and testing examples
    in the code.


    Args:
        number1: The first number.
        number2: The second number, which will be compared to number1.

    Returns:
        A string describing which number is the greatest.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> example_function(1, 2)
        1 is less than 2

    """
    if number1 < number2:
        return f"{number1} is less than {number2}"

    return f"{number1} is greater than or equal to {number2}"
