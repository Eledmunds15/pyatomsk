from pathlib import Path
from .core import run
from . import utils

def create(
    lattice: str,
    a: float,
    c: float = None,
    species: list[str] = None,
    orient: list[list[int]] = None,
    options: list[str] = None,
    output_file: str | Path = None,
    formats: list[str] = None
):
    """Create a standard lattice structure"""
    if species is None or len(species) == 0:
        raise ValueError("At least one atomic species must be specified.")

    if output_file:
        utils.checkExistingFile(output_file)

    cmd = ['--create', lattice, str(a)]
    if c is not None:
        cmd.append(str(c))
    cmd += species

    if orient is not None:
        cmd.append('orient')
        for vec in orient:
            cmd.append('[' + ''.join(map(str, vec)) + ']')

    if options:
        cmd += options

    if output_file:
        cmd.append(str(output_file))

    if formats:
        cmd += formats

    run(cmd)
    return Path(output_file) if output_file else None

def create_nanotube(
    a0: float,
    m: int,
    n: int,
    species: list[str],
    options: list[str] = None,
    output_file: str | Path = None,
    formats: list[str] = None
):
    """Create a nanotube structure using chiral indices m and n."""
    if species is None or len(species) == 0:
        raise ValueError("At least one atomic species must be specified.")
    if m is None or n is None:
        raise ValueError("Nanotubes require chiral indices m and n.")

    if output_file:
        utils.checkExistingFile(output_file)

    cmd = ['--create', 'nanotube', str(a0), str(m), str(n)] + species

    if options:
        cmd += options

    if output_file:
        cmd.append(str(output_file))

    if formats:
        cmd += formats

    run(cmd)
    return Path(output_file) if output_file else None

def merge(
    input_files: list[str | Path],
    output_file: str | Path,
    direction: str = None,
    options: list[str] = None,
    formats: list[str] = None
):
    """
    Merge multiple systems into one using Atomsk's --merge option.
    
    Parameters:
        input_files: List of paths to input files (at least 2)
        output_file: Path to the output file
        direction: Optional stacking direction ('x', 'y', or 'z')
        options: Additional Atomsk options to append
        formats: Optional list of formats for output
    
    Returns:
        Path: Path to the output file
    
    Raises:
        ValueError: If fewer than 2 input files are provided
        ValueError: If direction is invalid
    """
    if len(input_files) < 2:
        raise ValueError("At least two input files are required to merge.")

    output_file = Path(output_file)
    utils.checkExistingFile(output_file)

    # Ensure formats match
    for f in input_files:
        if not utils.checkFormatsMatch(f, output_file):
            raise ValueError(
                f"Input file format ({Path(f).suffix}) and output file format ({output_file.suffix}) do not match."
            )

    cmd = ['--merge']
    if direction:
        if direction.lower() not in ['x', 'y', 'z']:
            raise ValueError("Direction must be 'x', 'y', or 'z'.")
        cmd.append(direction.lower())

    # Number of files
    cmd.append(str(len(input_files)))

    # Add input files
    cmd += [str(f) for f in input_files]

    # Add output file
    cmd.append(str(output_file))

    # Optional formats
    if formats:
        cmd += formats

    # Additional options
    if options:
        cmd += options

    run(cmd)
    return output_file