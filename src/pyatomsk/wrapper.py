import subprocess
import shutil

class PyAtomskWorkflow:
    def __init__(self, executable="atomsk"):
        self.executable = shutil.which(executable)