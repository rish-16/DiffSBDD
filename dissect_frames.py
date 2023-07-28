import MDAnalysis as mda
import os, random

MD_HD5_PATH = "/data/rishabh/MD/h5_files/MD.hdf5"
md_obj = h5py.File(MD_HD5_PATH)

print (type(md_obj))
print (md_obj.keys())
for i, (key, items) in enumerate(md_obj.items()):
    print (key)
    print (items)

    if i == 5:
        break
