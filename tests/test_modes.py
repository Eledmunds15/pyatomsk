import os
import pyatomsk
from pathlib import Path

# ---------------------------
# Test for normal lattice creation
# ---------------------------
def test_create_normal_lattice(tmp_path):
    """
    Test the create() function for a standard lattice (FCC aluminum).
    """
    output_file = tmp_path / "al_system.cfg"

    pyatomsk.create(
        lattice='fcc',
        a=4.02,
        species=['Al'],
        output_file=output_file
    )

    # Check that Atomsk actually created the file
    assert output_file.exists()


# ---------------------------
# Test for normal lattice with options and orientation
# ---------------------------
def test_create_with_orientation_and_options(tmp_path):
    output_file = tmp_path / "al_supercell.cfg"

    pyatomsk.create(
        lattice='fcc',
        a=4.02,
        species=['Al'],
        orient=[[0, -1, 1], [1, 0, 0], [0, 1, 1]],
        options=['-duplicate', 2, 2, 2],
        output_file=output_file,
        formats=['lmp']
    )

    assert output_file.exists()


# ---------------------------
# Test for nanotube creation
# ---------------------------
def test_create_nanotube(tmp_path):
    """
    Test the create_nanotube() function for a simple carbon nanotube.
    """
    output_file = tmp_path / "nanotube.cfg"

    pyatomsk.create_nanotube(
        a0=2.5,
        m=8,
        n=8,
        species=['C'],
        output_file=output_file,
        formats=['cfg']
    )

    # Check that the file exists
    assert output_file.exists()


# ---------------------------
# Test for duplicate
# ---------------------------
def test_duplicate(tmp_path):
    """
    Test duplicating a lattice using create() and duplicate().
    """
    input_file = tmp_path / "unitcell.cfg"

    pyatomsk.create(
        lattice='fcc',
        a=4.02,
        species=['Al'],
        output_file=input_file
    )

    assert input_file.exists()

    output_file = tmp_path / "supercell.cfg"
    pyatomsk.duplicate(
        input_file=input_file,
        Nx=2,
        Ny=2,
        Nz=1,
        output_file=output_file
    )

    assert output_file.exists()


# ---------------------------
# Test for Merge
# ---------------------------
def test_merge(tmp_path):
    """
    Test the merge() function by merging two FCC lattices along the z-axis.
    """
    cwd = Path.cwd()
    os.chdir(tmp_path)

    try:
        # Create two FCC lattice files
        input_file1 = tmp_path / "unitcell1.cfg"
        input_file2 = tmp_path / "unitcell2.cfg"

        pyatomsk.create(
            lattice='fcc',
            a=4.02,
            species=['Al'],
            output_file=input_file1
        )

        pyatomsk.create(
            lattice='fcc',
            a=4.02,
            species=['Al'],
            output_file=input_file2
        )

        assert input_file1.exists()
        assert input_file2.exists()

        # Merge along z-axis, only pass filenames (Atomsk uses cwd)
        output_file_name = "merged_supercell.cfg"
        pyatomsk.merge(
            input_files=[input_file1.name, input_file2.name],
            output_file=output_file_name,
            direction='z',
            formats=['cfg']
        )

        # Check that the merged file exists in tmp_path
        output_file = tmp_path / output_file_name
        assert output_file.exists()

    finally:
        os.chdir(cwd)
