# Import libraries
import subprocess as sp
import shutil
from pathlib import Path

# === CHECK FOR ATOMSK EXECUTABLE === #

ATOMSK_EXEC = shutil.which("atomsk")

if ATOMSK_EXEC is None:
    raise FileNotFoundError(
        "Could not find the 'atomsk' executable in your system's PATH. "
        "Please ensure Atomsk is installed and added to your system's environment variables."
    )

# === CORE FUNCTIONS === #

def version():
    """Returns the version of the PyAtomsk and Atomsk executables."""
    result = run(["--version"])
    return result.stdout.strip()


def run(args):
    """Runs the Atomsk executable with the given arguments."""
    cmd = [ATOMSK_EXEC] + prepareArgs(args)
    print("Running command:", cmd)
    result = sp.run(cmd, capture_output=True, text=True, check=True)
    return result


def prepareArgs(args):
    """Ensures all arguments are strings for subprocess."""
    prepared = []
    for arg in args:
        if isinstance(arg, (str, bytes, int, float)):
            prepared.append(str(arg))
        elif isinstance(arg, Path):
            prepared.append(str(arg.resolve()))
        else:
            raise TypeError(f"Unsupported argument type: {type(arg)} for value {arg}")
    return prepared
