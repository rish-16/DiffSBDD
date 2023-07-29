import h5py
import numpy as np
import MDAnalysis as mda
import os, random

MD_HD5_PATH = "/data/rishabh/MD/h5_files/MD.hdf5"
md_obj = h5py.File(MD_HD5_PATH)

print (type(md_obj))
print (len(md_obj.keys()))
for i, (key, items) in enumerate(md_obj.items()):
    print (key, items)
    print (type(items), type(key))

    print (dict(items))

    if i == 3:
        break
