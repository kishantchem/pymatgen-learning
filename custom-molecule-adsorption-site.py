import numpy as np
from pymatgen.core import Structure
from pymatgen.core.surface import SlabGenerator
from pymatgen.core import Molecule
import matplotlib.pyplot as plt
from pymatgen.analysis.adsorption import plot_slab
from pymatgen.analysis.adsorption import AdsorbateSiteFinder

# Load the CIF file
slab = Structure.from_file("Pt_111_2x2.cif")

# Define a custom adsorption site manually (example: a site between hollow and bridge)
custom_site = np.array([6.0, 4.0, 20.0])  # Modify coordinates as needed

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

# Define an H₂O molecule (Oxygen at origin, Hydrogens nearby)
h2o = Molecule(["O", "H", "H"], [[0, 0, 0], [0.96, 0.0, 0.0], [-0.32, 0.92, 0.0]])


# Place H₂O at the adsorption site
adsorbed_slab = asf.add_adsorbate(h2o, custom_site, translate=True)

# Save the new structure with adsorbate
adsorbed_slab.to("custom_adsorbed_structure.cif")

# Print confirmation
print("H₂O placed on the adsorption site and structure saved as 'custom_adsorbed_structure.cif'")
