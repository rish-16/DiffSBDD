import os, re, subprocess, json, csv
from pprint import pprint
import MDAnalysis as mda
from MDAnalysis.analysis import align

uni = mda.Universe("3L9H_MD_frame61.pdb", format="PDB")
print (uni.chain)
print (uni)
mol_atoms = uni.select_atoms("resname MOL")
print (mol_atoms[0].resid)
print (mol_atoms[0])