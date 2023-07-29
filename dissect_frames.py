import h5py
import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis import rms
import os, random

MD_HD5_PATH = "/data/rishabh/MD/h5_files/MD.hdf5"
md_obj = h5py.File(MD_HD5_PATH)

proteins = []
frames = []

for i, (key, items) in enumerate(md_obj.items()):
    proteins.append(key)

    n_atoms = len(items['atoms_element'])
    coordinates = items['trajectory_coordinates']
    frames.append(np.array(coordinates))

    if i == 3:
        break

# print (frames[0])
# print (type(frames[0]))
# print (frames[0].shape)

protein = proteins[0]
sample_coords = frames[0]
seen = ()
scores = []

for fi in range(sample_coords.shape[0]):
    for fj in range(sample_coords.shape[0]):
        temp = []
        if fi != fj:
            r = rms.rmsd(sample_coords[fi], sample_coords[fj], center=True, superposition=True)
            temp.append(r)
        else:
            temp.append(0)
        scores.append(temp)

np.save("scores.npy", np.array(scores))

"""
10GS <HDF5 group "/10GS" (10 members)>
<class 'h5py._hl.group.Group'> <class 'str'>
{
    'atoms_element': <HDF5 dataset "atoms_element": shape (6593,), type "<i8">, 
    'atoms_number': <HDF5 dataset "atoms_number": shape (6593,), type "<i8">, 
    'atoms_residue': <HDF5 dataset "atoms_residue": shape (6593,), type "<i8">, 
    'atoms_type': <HDF5 dataset "atoms_type": shape (6593,), type "<i8">, 
    'frames_bSASA': <HDF5 dataset "frames_bSASA": shape (100,), type "<f8">, 
    'frames_distance': <HDF5 dataset "frames_distance": shape (100,), type "<f8">, 
    'frames_interaction_energy': <HDF5 dataset "frames_interaction_energy": shape (100,), type "<f8">, 
    'frames_rmsd_ligand': <HDF5 dataset "frames_rmsd_ligand": shape (100,), type "<f8">, 
    'molecules_begin_atom_index': <HDF5 dataset "molecules_begin_atom_index": shape (3,), type "<i8">, 
    'trajectory_coordinates': <HDF5 dataset "trajectory_coordinates": shape (100, 6593, 3), type "<f8">
}
"""
