import torch
import MDAnalysis as mda
import torch_geometric as tg
import numpy as np

# def get_ligand_mask():


def extract_ligand_orthocenter(coordinates, ligand_mask):
    pass

def get_binding_pocket_residues(ligand_orthocenter, coordinates, residues, atom_types, bbox_thres=22):
    pass

class MISATOPocketLigandDataset(tg.data.Dataset):
    def __init__(self):
        pass

def main(trajectory_coordinates, atom_types, residue_types):
    assert len(residue_types) == len(atom_types)


mdh5_file = '/data/rishabh/MD/h5_files/MD.hdf5'
md_H5File = h5py.File(mdh5_file)

pdb_codes = list(dict(md_H5File).keys())
print ("number of PDBs:", len(pdb_codes))

pprint (md_H5File['1A4G'].keys())
print (md_H5File['1A4G/atoms_residue'][:])