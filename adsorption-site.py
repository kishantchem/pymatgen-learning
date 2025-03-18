from pymatgen.core import Structure
from pymatgen.analysis.adsorption import AdsorbateSiteFinder
from pymatgen.core.surface import SlabGenerator
from pymatgen.core import Molecule
import matplotlib.pyplot as plt
from pymatgen.analysis.adsorption import plot_slab

# Load the CIF file
slab = Structure.from_file("Pt_111_2x2.cif")

# Initialize Adsorbate Site Finder
asf = AdsorbateSiteFinder(slab)

# Get all adsorption sites
adsorption_sites = asf.find_adsorption_sites()
print("Adsorption Sites:", adsorption_sites)

# Define colors for adsorption site types
site_colors = {"ontop": "red", "bridge": "blue", "hollow": "green"}

# Extract atomic positions projected onto the XY plane
x_atoms = [site.x for site in slab.sites]  # X-coordinates of atoms
y_atoms = [site.y for site in slab.sites]  # Y-coordinates of atoms

# Create a figure
fig, ax = plt.subplots(figsize=(6, 6))

# Plot slab atoms (gray circles)
ax.scatter(x_atoms, y_atoms, color="gray", s=200, edgecolors="black", label="Atoms")

# Plot adsorption sites
for site_type, positions in adsorption_sites.items():
    if site_type in site_colors and positions:  # Ensure valid site type and non-empty positions
        x_coords = [pos[0] for pos in positions]  # X-coordinates
        y_coords = [pos[1] for pos in positions]  # Y-coordinates
        ax.scatter(x_coords, y_coords, color=site_colors[site_type], label=f"{site_type.capitalize()} Sites", edgecolors='black', s=150)

# Set axis labels and title
ax.set_xlabel("X-axis (Å)")
ax.set_ylabel("Y-axis (Å)")
ax.set_title("Top-Down View of Slab with Adsorption Sites")
ax.legend()

# Show the plot
plt.savefig("adsorption_sites.png", dpi=300, bbox_inches='tight')
plt.show()

