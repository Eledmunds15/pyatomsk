from pathlib import Path
from . import utils
from .core import run

def duplicate(
    input_file: str | Path,
    Nx: int = 1,
    Ny: int = 1,
    Nz: int = 1,
    output_file: str | Path = None,
    sort: bool = False
):
    """Duplicate a system in three directions using Atomsk's -duplicate option."""
    input_path = Path(input_file)

    if output_file is None:
        output_file = input_path.with_name(input_path.stem + "_dup" + input_path.suffix)
    else:
        output_file = Path(output_file)

    utils.checkExistingFile(output_file)
    utils.checkFormatsMatch(input_path, output_file)

    cmd = [str(input_path), '-duplicate', str(Nx), str(Ny), str(Nz)]
    cmd.append(str(output_file))

    run(cmd)
    return output_file

def deform(
    input_file: str | Path,
    component: str,
    strain: float | str,
    poisson: float = None,
    output_file: str | Path = None
):
    """
    Apply uniaxial or shear deformation to a system using Atomsk's -deform option.

    Parameters:
        input_file: Path to the input structure file
        component: Deformation component ('x', 'y', 'z' for uniaxial, or
                   'xy', 'xz', 'yz', 'yx', 'zx', 'zy' for shear)
        strain: Strain value (e.g., 0.06 for 6%) or 'untilt' for shear tilt correction
        poisson: Optional Poisson's ratio (only valid for uniaxial deformation)
        output_file: Path to the output file

    Returns:
        Path: Path to the deformed output file
    """
    input_file = Path(input_file)

    # Default output filename if not provided
    if output_file is None:
        output_file = input_file.with_name(input_file.stem + "_def" + input_file.suffix)
    else:
        output_file = Path(output_file)

    # Check formats
    if not utils.checkFormatsMatch(input_file, output_file):
        raise ValueError(
            f"Input format ({input_file.suffix}) and output format ({output_file.suffix}) do not match."
        )

    # Ensure output file doesn't already exist
    utils.checkExistingFile(output_file)

    # Build Atomsk command
    cmd = [str(input_file), '-deform', component, str(strain)]
    if poisson is not None:
        cmd.append(str(poisson))
    cmd.append(str(output_file))

    # Run Atomsk
    run(cmd)

    return output_file