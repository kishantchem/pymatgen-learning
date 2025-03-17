from pymatgen.core import Structure
from pymatgen.core.surface import SlabGenerator
from ase.visualize import view
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.core import Lattice
from pymatgen.vis.structure_vtk import StructureVis

# Load the CIF file
structure = Structure.from_file("platinum.cif")


# Define Miller indices for the surface
miller_index = (1, 1, 1)

# Generate slab
slabgen = SlabGenerator(
    initial_structure=structure,
    miller_index=miller_index,
    min_slab_size=6,  # Thickness of the slab (in Å)
    min_vacuum_size=15,  # Vacuum layer (in Å)
    lll_reduce=True,  # Reduce structure using LLL algorithm
    center_slab=True  # Center slab in the unit cell
)

# Get the generated slabs


slabs = slabgen.get_slabs()
length_slab=len(slabs)
print("length_slab=", length_slab)
# Select the first slab
slab = slabs[0]
print(slab)

# Save slab to a CIF file
slab.to(filename="slab_111.cif", fmt="cif")

# Save slab in VASP POSCAR format
slab.to(fmt="poscar", filename="POSCAR_slab")

atoms = AseAtomsAdaptor.get_atoms(slab)
##view(atoms)


# Create a 2×2 supercell
supercell = slab.make_supercell([ [10,0,0], [0,10,0], [0,0,1] ])  

# Print details of the supercell
print("Supercell dimensions:", supercell.lattice)
print("Number of atoms in supercell:", len(supercell.sites))

# Save as CIF file
supercell.to(fmt="cif", filename="Pt_111_2x2.cif")

# Save as PDB file
supercell.to(fmt="pdb", filename="Pt_111_2x2.pdb")

# Save as POSCAR for VASP
supercell.to(fmt="poscar", filename="POSCAR_Pt_111_2x2")

# Convert to ASE object
atoms = AseAtomsAdaptor.get_atoms(supercell)

# View structure
##view(atoms)


# View structure using VTK
vis = StructureVis()
vis.set_structure(supercell)
vis.show()
