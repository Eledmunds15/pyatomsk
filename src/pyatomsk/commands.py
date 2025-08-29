import subprocess
import shutil

from pathlib import Path

ATOMSK_EXEC = shutil.which("atomsk")

# === CLI INTERFACE ===

def version():

    result = run(["--version"])
    
    return result.stdout.strip()
    
def run(args):

    cmd = [ATOMSK_EXEC] + args

    # Run tests on CMD to check whether it is suitable for subprocess
    cmd = prepare_subprocess_args(cmd)

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def prepare_subprocess_args(args):

    prepared = []
    for arg in args:
        if isinstance(arg, (str, bytes)):
            prepared.append(str(arg))
        elif isinstance(arg, (int, float)):
            prepared.append(str(arg))
        elif isinstance(arg, Path):
            prepared.append(str(arg.resolve()))
        else:
            raise TypeError(f"Unsupported argument type: {type(arg)} for value {arg}")
    return prepared

def convert(inputFile, outputFormat):

    return None

def create(crysStruc, latParam, material, outputFile):

    result = run(['--create'] + [crysStruc, latParam, material, outputFile])

# Modes

# Options

# Formats

