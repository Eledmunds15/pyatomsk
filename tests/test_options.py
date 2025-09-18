import pyatomsk
from pathlib import Path

# TO DO: Add tests for add_atom, check add_atom.

# ---------------------------
# Test duplicate function
# ---------------------------
def test_duplicate(tmp_path):
    """
    Test duplicating a lattice using create() and duplicate().
    """
    # Create lattice input
    input_file = tmp_path / "unitcell.cfg"
    pyatomsk.create(
        lattice='fcc',
        a=4.02,
        species=['Al'],
        output_file=input_file
    )

    # Check unitcell exists
    assert input_file.exists()

    # Duplicate lattice
    output_file = tmp_path / "supercell.cfg"
    pyatomsk.duplicate(
        input_file=input_file,
        Nx=2,
        Ny=2,
        Nz=1,
        output_file=output_file
    )

    # Check supercell exists
    assert output_file.exists()

# ---------------------------
# Test for deform
# ---------------------------
def test_deform(tmp_path):
    """
    Test the deform() function for both uniaxial and shear deformation.
    """
    # Step 1: create a simple FCC lattice as input
    input_file = tmp_path / "unitcell.cfg"
    pyatomsk.create(
        lattice='fcc',
        a=4.02,
        species=['Al'],
        output_file=input_file
    )

    # Check input file exists
    assert input_file.exists()

    # Step 2: uniaxial deformation along X
    output_file_x = tmp_path / "unitcell_def_x.cfg"
    pyatomsk.deform(
        input_file=input_file,
        component='x',
        strain=0.01,   # 1% tensile strain
        poisson=0.0,
        output_file=output_file_x
    )

    # Check the output file exists
    assert output_file_x.exists()

    # Step 3: shear deformation along xy
    output_file_xy = tmp_path / "unitcell_def_xy.cfg"
    pyatomsk.deform(
        input_file=input_file,
        component='xy',
        strain=0.005,  # 0.5% shear
        output_file=output_file_xy
    )

    # Check the output file exists
    assert output_file_xy.exists()
