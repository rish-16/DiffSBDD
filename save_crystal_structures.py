import os, subprocess, csv, json, re
import MDAnalysis as mda
from pprint import pprint

BM2020_PATH = "/data/rishabh/BindingMOAD_2020/"
OVERLAP_PATH = "PDB_IDs/misato_moad_pocket_info.txt"

with open(OVERLAP_PATH, "r") as f:
    overlap_records = f.read().strip().split("\n")[1:] # ignore header
    overlap_records = [rec.strip().split(",") for rec in overlap_records]

converter = lambda s : re.findall(r'\d', s.split("_")[0])[0]

overlap_PDBs = {
    rec[0].upper() : rec[2]
    for rec in overlap_records
}

original_structures = {}
for pdb in os.listdir(BM2020_PATH):
    if "_1" in pdb or "_2" in pdb or "_3" in pdb:
        pdb_ = pdb[:-6] # ignore the _x.pdb prefix
        if pdb_.upper() in overlap_PDBs:
            if pdb_.upper() in original_structures:
                original_structures[pdb_].append([pdb, overlap_PDBs[pdb_.upper()]])
            else:
                original_structures[pdb_] = [[pdb, overlap_PDBs[pdb_.upper()]]]
    
for key, val in original_structures.items():
    fp = BM2020_PATH + val[0][0]
    # cmd = f"cp {fp} og_crystal_structs/{val[0]}"
    # subprocess.call(cmd, shell=True)
    print (f"{key.upper()}, {BM2020_PATH + val[0][0]}, {val[0][1]}")