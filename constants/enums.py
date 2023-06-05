from enum import Enum


class PythonCliCommand(Enum):
    """
    This enum is used to describe the command
    which will be used in the command line to
    spin up the python interpretor
    """
    PYTHON = "python"
    PYTHON3 = "python3"
