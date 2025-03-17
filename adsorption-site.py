from pymatgen.core import Structure
from pymatgen.analysis.adsorption import AdsorbateSiteFinder
from pymatgen.core.surface import SlabGenerator
from pymatgen.core import Molecule

# Load the CIF file
structure = Structure.from_file("Pt_111_2x2.cif")

# Initialize Adsorbate Site Finder
asf = AdsorbateSiteFinder(structure)

# Get all adsorption sites
adsorption_sites = asf.find_adsorption_sites()
print("Adsorption Sites:", adsorption_sites)
