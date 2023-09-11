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

pprint (md_H5File['1A4G'].keys())
print (md_H5File.get('1A4G/frames_distance')[:20])
print (md_H5File.get('1A4G/frames_distance').shape)
print (md_H5File.get('1A4G/frames_rmsd_ligand')[:20])
print (md_H5File.get('1A4G/frames_rmsd_ligand').shape)


pprint (md_H5File['1CNX'].keys())
# print (md_H5File.get('1CNX/atoms_coordinates_ref')[:])
# print (md_H5File.get('1CNX/atoms_element')[:20])
# print (md_H5File.get('1CNX/atoms_residue')[:20])
# print (md_H5File.get('1CNX/atoms_number')[:20])