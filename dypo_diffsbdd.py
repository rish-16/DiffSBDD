"""
- open PDB
- get pairwise RMSD between all frames
- extract top-K distinct frames
- save separate PDBs for each frame (along with the ligand molecule)
- run DiffSBDD on each frame PDB
- examine K different molecules
"""

import MDAnalysis as mda
import numpy as np

pdb_path = ""

def pairwise_rmsd(universe):
    trajectory = universe.trajectory
    frame_i = trajectory[0]
    frame_j = trajectory[j]
