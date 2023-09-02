"""
- open PDB
- get pairwise RMSD between all frames
- extract top-K distinct frames
- save separate PDBs for each frame (along with the ligand molecule)
- run DiffSBDD on each frame PDB
- examine K different molecules
"""

import MDAnalysis as mda
from MDAnalysis.analysis import diffusionmap, align, rms
import matplotlib.pyplot as plt
import numpy as np

pdb_path = "misato/1A4G_final_animation.pdb"

def pairwise_rmsd(universe, K):
    trajectory = universe.trajectory
    universe.trajectory[0]
    aligner = align.AlignTraj(universe, universe, select='name CA', in_memory=True).run()
    matrix = diffusionmap.DistanceMatrix(universe, select='name CA').run()

    # plt.imshow(matrix.dist_matrix, cmap='viridis')
    # plt.xlabel('Frame')
    # plt.ylabel('Frame')
    # plt.colorbar(label=r'RMSD ($\AA$)')
    # plt.show()

    rmsd_sum = matrix.dist_matrix.sum(axis=0)

    ind = np.argpartition(rmsd_sum, -K)[-K:]
    return ind.tolist()

universe = mda.Universe(pdb_path, format="PDB")
topk_index = pairwise_rmsd(universe, K=10)

n_atoms = universe.atoms

for fi in topk_index:
    frame = universe.trajectory[fi]
    print (frame.time, fi)
    with mda.Writer(f"1A4G_complex_frame_{str(fi)}.pdb", n_atoms=n_atoms) as W:
        W.write(universe.atoms)
