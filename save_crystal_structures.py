import os, subprocess, csv, json, re
import MDAnalysis as mda
from pprint import pprint

BM2020_PATH = "/data/rishabh/BindingMOAD_2020/"
OVERLAP_PATH = "PDB_IDs/misato_moad_pocket_info.txt"

with open(OVERLAP_PATH, "r") as f:
    overlap_records = f.read().strip().split("\n")[1:] # ignore header
    overlap_records = [rec.strip().split(",") for rec in overlap_records]

converter = lambda s : re.findall("r'\d+'", s.split("_")[0])[0]

overlap_PDBs = {
    (rec[0].upper(), converter(rec[1])) : True
    for rec in overlap_records
}

pprint (overlap_PDBs)
print (len(overlap_PDBs))

# original_structures = {}
# for pdb in os.listdir(BM2020_PATH):
#     if "_1" in pdb or "_2" in pdb or "_3" in pdb:
#         pdb_ = pdb[:-6] # ignore the _x.pdb prefix
#         if (pdb_.upper(), ) in overlap_PDBs:
#             if pdb_.upper() in original_structures:
#                 original_structures[pdb_].append(pdb)
#             else:
#                 original_structures[pdb_] = [pdb]
    
# print (original_structures)