import os, subprocess, csv, json
import MDAnalysis as mda

BM2020_PATH = "/data/rishabh/BindingMOAD_2020/"
OVERLAP_PATH = "PDB_IDs/misato_moad_pocket_info.txt"

with open(OVERLAP_PATH, "r") as f:
    overlap_records = f.read().strip().split("\n")[1:] # ignore header
    overlap_records = [rec.strip().split(",") for rec in overlap_records]

overlap_PDBs = {
    rec[0].upper() : True
    for rec in overlap_records
}

print (len(overlap_PDBs))

original_structures = {}
for pdb in os.listdir(BM2020_PATH):
    if "_1" in pdb or "_2" in pdb or "_3" in pdb:
        pdb_ = pdb[:-6] # ignore the _x.pdb prefix
        if pdb_.upper() in overlap_PDBs:
            if pdb_.upper() in original_structures:
                original_structures[pdb_].append(pdb)
            else:
                original_structures[pdb_] = [pdb]
    
print (original_structures)