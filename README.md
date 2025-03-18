# PYMATGEN Learning

## Introduction
[PYMATGEN](https://pymatgen.org/) (Python Materials Genomics) is a powerful Python library for materials science, enabling analysis, structure manipulation, and electronic structure calculations.

This guide provides step-by-step instructions to set up PYMATGEN in a **Conda environment** along with necessary dependencies.

## Installation

### 1. Create a Conda Environment
```bash
conda env list  # Check existing environments
conda create --name pymatgen python=3.9  # Create a new environment
conda activate pymatgen  # Activate the environment
```

### 2. Install PYMATGEN and Prerequisites
```bash
conda install -c conda-forge pymatgen  # Install PYMATGEN
conda install -c conda-forge openbabel  # Install OpenBabel (for molecular file handling)
conda install -c conda-forge ase  # Install ASE (Atomic Simulation Environment)
conda install -c conda-forge vtk  # Install VTK (for visualization)
```

## Verifying Installation
Run the following Python commands to check if PYMATGEN and dependencies are correctly installed:
```python
import pymatgen
import ase
import vtk
import openbabel
print("All packages imported successfully!")
```
If no errors appear, the installation is successful.

## Usage Examples

### 1. Load a Structure from a CIF File
```python
from pymatgen.core import Structure
structure = Structure.from_file("example.cif")
print(structure)
```

### 2. Generate a Slab Model
```python
from pymatgen.core.surface import SlabGenerator
slab = SlabGenerator(structure, miller_index=(1,1,1), min_slab_size=10, min_vacuum_size=15).get_slab()
print(slab)
```

### 3. Find Adsorption Sites on a Surface
```python
from pymatgen.analysis.adsorption import AdsorbateSiteFinder
asf = AdsorbateSiteFinder(slab)
adsorption_sites = asf.find_adsorption_sites()
print("Adsorption Sites:", adsorption_sites)
```

## Saving and Visualizing Structures

### Save Structure to a File
```python
structure.to(filename="output.cif")
```

### Plot a Slab Structure
```python
import matplotlib.pyplot as plt
from pymatgen.analysis.adsorption import plot_slab
plot_slab(slab, plt.gca())
plt.show()
```

## Additional Resources
- **PYMATGEN Documentation:** [https://pymatgen.org/](https://pymatgen.org/)
- **Materials Project API:** [https://materialsproject.org/](https://materialsproject.org/)

## License
This project follows the **MIT License**.

---
This README provides a basic **PYMATGEN setup guide** along with **usage examples**. Feel free to expand it based on your learning journey! 🚀


