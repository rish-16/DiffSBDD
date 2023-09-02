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
from MDAnalysis.coordinates.PDB import PDBWriter
import matplotlib.pyplot as plt
import numpy as np

pdb_path = "misato/1CNX_final_animation.pdb"

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

universe = mda.Universe(pdb_path, format="PDB", guess_bonds=True, guess_topology=True)
topk_index = pairwise_rmsd(universe, K=10)

guessed_bonds = mda.topology.guessers.guess_bonds(universe.atoms, universe.atoms.positions)
print (guessed_bonds)
universe.add_TopologyAttr('bonds', guessed_bonds)

n_atoms = universe.atoms

for fi in topk_index:
    frame = universe.trajectory[fi]
    print (frame.time, fi)
    with PDBWriter(f"misato/1CNX_frames/1CNX_complex_frame_{str(fi)}.pdb", n_atoms=n_atoms, bonds='conect',) as W:
        W.write(universe)
        
        # try:
        #     print (universe.__dict__.keys())
        #     W.write(universe.bonds)
        # except Exception as e:
        #     print (e)
