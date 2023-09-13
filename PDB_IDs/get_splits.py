import os
from pprint import pprint

moad_path = "binding_moad_test.txt"
misato_path = "misato.txt"

with open(moad_path, "r") as f:
    moad_ids = f.read().strip().split("\n")
    moad_ids = set([id_.strip() for id_ in moad_ids])

with open(misato_path, "r") as f:
    misato_ids = f.read().strip().split("\n")
    misato_ids = set([id_.strip() for id_ in misato_ids])

overlap = moad_ids.intersection(misato_ids)
pprint (list(overlap))

# moad_ids_unique = moad_ids.difference(misato_ids)
# print (len(moad_ids_unique))

# misato_unique = misato_ids.difference(moad_ids)
# print (len(misato_unique))

with open("moadtest_misatoall_overlap.txt", "a+") as f:
    for o in overlap:
        f.write(f"{o}\n")
