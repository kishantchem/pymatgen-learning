from pymatgen.core import Structure
from pymatgen.io.espresso.inputs import pwin as pwin

# Load structure from a CIF file
structure = Structure.from_file("adsorbed_structure.cif")  # Change to your file

# Define Quantum ESPRESSO input parameters
input_data = {
    "&control": {
        "calculation": "scf",  # Self-consistent field calculation
        "prefix": "qe_calc",
        "pseudo_dir": "./pseudo",  # Directory for pseudopotentials
        "outdir": "./out",
        "tprnfor": True,  # Print forces
        "tstress": True   # Print stress tensor
    },
    "&system": {
        "ecutwfc": 50,  # Plane-wave cutoff energy (Ry)
        "ecutrho": 400, # Charge density cutoff (Ry)
        "occupations": "smearing",
        "smearing": "gaussian",
        "degauss": 0.02
    },
    "&electrons": {
        "conv_thr": 1.0e-6,
        "mixing_beta": 0.7
    }
}

# Define pseudopotentials (modify based on your structure)
pseudo = {
    "Pt": "Pt.pbe-n-kjpaw_psl.1.0.0.UPF",
    "O": "O.pbe-n-kjpaw_psl.1.0.0.UPF",
    "H": "H.pbe-n-kjpaw_psl.1.0.0.UPF"
}

# Define k-point grid
kpoints_grid = (4, 4, 1)

# Create PWin object
qe_input = pwin(
    Structure=structure,
    input_data=input_data,
    pseudopotentials=pseudo,
    kpoints_mode="automatic",
    kpoints_grid=kpoints_grid
)

# Write QE input file
qe_input.write_file("qe_input.in")

print("Quantum ESPRESSO input file 'qe_input.in' generated successfully!")

