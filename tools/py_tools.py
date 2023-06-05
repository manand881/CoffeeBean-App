import shutil
from constants.enums import PythonCliCommand
from constants.globals import python_version


def is_python3():
    """
    Check if Python 3.x is being used
    """
    return python_version == 3


def has_python3():
    """
    Check if "python3" command is available
    """
    return bool(shutil.which(PythonCliCommand.PYTHON3.value))


def appropriate_python_cmd():
    """
    Use the appropriate command based on the Python version
    """
    if is_python3() and has_python3():
        return PythonCliCommand.PYTHON3.value
    else:
        return PythonCliCommand.PYTHON.value
