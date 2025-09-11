from pathlib import Path

def checkExistingFile(output_file: str | Path):
    """Raises an error if the requested output file already exists."""
    output_path = Path(output_file)
    if output_path.exists():
        raise FileExistsError(f"The output file '{output_path}' already exists.")
    return True

def checkFormatsMatch(input_file, output_file):
    """Checks whether the input and output file formats match."""
    input_ext = Path(input_file).suffix.lower()
    output_ext = Path(output_file).suffix.lower()

    if input_ext != output_ext:
        raise ValueError(
            f"Input file format ({input_file.suffix}) and output file format ({output_file.suffix}) do not match."
        )
    else:
        return True