import os
import sys
from tools.py_tools import appropriate_python_cmd


def restart():
    print("\nRestarting application...")
    filename = __file__.split("\\")
    python_cmd = appropriate_python_cmd()
    os.system(f"{python_cmd} "+filename[-1])
    sys.exit()
