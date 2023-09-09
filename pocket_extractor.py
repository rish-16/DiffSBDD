import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import MDAnalysis as mda
import h5py
import os, subprocess

mdh5_file = '/data/rishabh/MD/h5_files/MD.hdf5'
md_H5File = h5py.File(mdh5_file)

pdb_codes = list(dict(md_H5File).keys())
print ("number of PDBs:", len(pdb_codes))

print (md_H5File['1A4G'].keys())