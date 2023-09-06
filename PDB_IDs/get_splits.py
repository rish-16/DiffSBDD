import os

crossdocked_path = "crossdocked2020.txt"
misato_path = "misato.txt"

with open(crossdocked_path, "r") as f:
    cd_ids = f.read().strip().split("\n")
    cd_ids = set([id_.strip() for id_ in cd_ids])

with open(misato_path, "r") as f:
    misato_ids = f.read().strip().split("\n")
    misato_ids = set([id_.strip() for id_ in misato_ids])

overlap = cd_ids.intersection(misato_ids)
print (len(overlap))

cd_ids_unique = cd_ids.difference(misato_ids)
print (len(cd_ids_unique))

misato_unique = misato_ids.difference(cd_ids)
print (len(misato_unique))