import pyatomsk
from pyatomsk import commands as cmd

def main():

    # Print Info
    print("PyAtomsk Version: ")
    print(pyatomsk.__version__)

    print("Atomsk Version: ")
    print(cmd.version())

    cmd.create('fcc', 4.046, 'Al', 'Aluminium.cfg')

    return None

if __name__ == "__main__":

    main()