import os, csv
import pandas as pd

gpcrmd_path = "gpcrmd.csv"
gpcr_data = pd.read_csv(gpcrmd_path)['PDB_ID'].values.tolist()
gpcr_data = set([g.strip().upper() for g in gpcr_data])

# print (gpcr_data)

with open("moadtest_misatoall_overlap.txt", "r") as f:
    moad_misato_overlap = f.read().strip().split("\n")
    moad_misato_overlap = [r.strip().upper() for r in moad_misato_overlap]

moad_misato_overlap = set(moad_misato_overlap)

print (gpcr_data.intersection(moad_misato_overlap))
print (moad_misato_overlap.intersection(gpcr_data))