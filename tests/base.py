from pathlib import Path
import pyatomsk

def main():
    # ---------------------------
    # File paths
    # ---------------------------
    unitcell_file = Path("Al_unitcell.cfg")
    bottom_file = Path("bottom.cfg")
    top_file = Path("top.cfg")
    bicrystal_file = Path("Al_edge_bicrystal.cfg")

    # ---------------------------
    # Step 0: Create the unit cell
    # ---------------------------
    pyatomsk.create(
        lattice='fcc',
        a=4.02,
        species=['Al'],
        output_file=unitcell_file
    )

    # ---------------------------
    # Step 1: Create the bottom crystal
    # Duplicate 40 x 10 x 1
    # ---------------------------
    bottom_dup = Path("bottom_dup.cfg")
    pyatomsk.duplicate(
        input_file=unitcell_file,
        Nx=40,
        Ny=10,
        Nz=1,
        output_file=bottom_dup
    )

    # Apply pure tensile strain along X (Poisson ratio = 0)
    pyatomsk.deform(
        input_file=bottom_dup,
        component='x',
        strain=0.0125,
        poisson=0.0,
        output_file=bottom_file
    )

    # ---------------------------
    # Step 2: Create the top crystal
    # Duplicate 41 x 10 x 1
    # ---------------------------
    top_dup = Path("top_dup.cfg")
    pyatomsk.duplicate(
        input_file=unitcell_file,
        Nx=41,
        Ny=10,
        Nz=1,
        output_file=top_dup
    )

    # Apply compression along X
    pyatomsk.deform(
        input_file=top_dup,
        component='x',
        strain=-0.012195122,
        poisson=0.0,
        output_file=top_file
    )

    # ---------------------------
    # Step 3: Merge the two crystals along Y
    # ---------------------------
    pyatomsk.merge(
        input_files=[bottom_file, top_file],
        output_file=bicrystal_file,
        direction='Y',
        formats=['cfg']
    )

    print(f"Bicrystal created: {bicrystal_file}")

if __name__ == "__main__":
    main()
