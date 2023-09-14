"""
- find PDBs from the MOAD test set that are also in MISATO/PDBBind
- extract frames from the PDB
- keep track of RMSD from crystal structure
"""

import os, re, subprocess
from pprint import pprint
import h5py

PATH = "PDB_IDs/moadtest_misatoall_overlap.txt"
H5_PATH = "/data/rishabh/MD/h5_files/MD.hdf5"
h5_file = h5py.File(H5_PATH)

with open(PATH, "r") as f:
    pdb_ids = f.read().strip().split("\n")
    pdb_ids = [d.strip() for d in pdb_ids]

for pdb in pdb_ids:
    record = h5_file[pdb]
    for i in range(100):
        cmd = f"python h5_to_pdb.py -s {pdb.upper()} -dMD {H5_PATH} -f {i} -o analysis_combined_pdbs/combined_{pdb.upper()}/"
        subprocess.call(cmd, shell=True)

