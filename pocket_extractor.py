import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import MDAnalysis as mda
import h5py
import os, subprocess

mdh5_file = 'misato/all_atoms_11GS.hdf5'
md_H5File = h5py.File(mdh5_file)

pdb_codes = list(dict(md_H5File).keys())
print ("number of PDBs:", len(pdb_codes))

print (md_H5File['11GS'].keys())
print (md_H5File.get('11GS/atoms_coordinates_ref')[:])
print (md_H5File.get('11GS/atoms_element')[:200])
print (md_H5File.get('11GS/atoms_residue')[:200])
print (md_H5File.get('11GS/atoms_number')[:200])

