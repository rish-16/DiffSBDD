import os, random, h5py
import MDAnalysis as mda
from MDAnalysis.analysis import diffusionmap, align, rms
from MDAnalysis.coordinates.PDB import PDBWriter
import matplotlib.pyplot as plt
import numpy as np

# MD_HD5_PATH = "/data/rishabh/MD/h5_files/MD.hdf5"
# md_obj = h5py.File(MD_HD5_PATH)

PATH = "all_misato_anim/"
md_folder = os.listdir(PATH)

def pairwise_rmsd(universe, K):
    trajectory = universe.trajectory
    universe.trajectory[0]
    aligner = align.AlignTraj(universe, universe, select='name CA', in_memory=True).run()
    matrix = diffusionmap.DistanceMatrix(universe, select='name CA').run()
    rmsd_sum = matrix.dist_matrix.sum(axis=0)
    return rmsd_sum

mean_array = []
median_array = []
for pdb in md_folder:
    pdb_path = PATH + pdb
    universe = mda.Universe(pdb_path, format="PDB", guess_bonds=True, guess_topology=True)
    all_frames_cumulative_rmsd = pairwise_rmsd(universe, K=10)
    n_atoms = universe.atoms
    n_frames = len(universe.trajectory)
    mean_array.append(all_frames_cumulative_rmsd.mean() / n_frames)
    median_array.append(np.median(all_frames_cumulative_rmsd) / n_frames)

fig = plt.figure()
plt.hist(mean_array, bins=20, color="orange")
plt.xlabel("Mean Frame-wise Cumulative RMSD")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("mean_framewise_cumulative_rmsd.pdf")

fig = plt.figure()
plt.hist(median_array, bins=20, color="blue")
plt.xlabel("Median Frame-wise Cumulative RMSD")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("median_framewise_cumulative_rmsd.pdf")