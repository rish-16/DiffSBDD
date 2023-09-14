import os
from pprint import pprint

with open("PDB_IDs/binding_moad_test.txt", "r") as f:
    moad_misato_pdb_list = f.read().strip().split("\n")
    moad_misato_pdb_list = [d.strip() for d in moad_misato_pdb_list]

with open("data/moad_test.txt", "r") as f:
    moad_test = f.read().strip().split(",")
    moad_test = [d.split("-") for d in moad_test]
    moad_test = [[rec[0], rec[1].split("_")] for rec in moad_test]
    moad_test = [[rec[0], rec[1][0], rec[1][1].split(":")] for rec in moad_test]
    moad_test = [[rec[0], rec[1], rec[2][0], rec[2][1] + ":" + rec[2][2]] for rec in moad_test]
    moad_test = {
        rec[0] : [rec[1] + "_" + rec[2], rec[3]]
        for rec in moad_test
    }

print (f"PDBID,LigID,ChainInfo")
for pdb in moad_misato_pdb_list:
    if pdb in moad_test:
        pdb_details = moad_test[pdb]
        print (f"{pdb},{pdb_details[0]},{pdb_details[1]}")