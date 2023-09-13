import re
from pprint import pprint

with open("../data/moad_test.txt", "r") as f:
    moad_data = f.read().strip().split(",")
    moad_data = [d.strip().split("-")[0].strip() for d in moad_data]

moad_data = list(set(moad_data))

with open("binding_moad.txt", "w+") as f:
    for d in moad_data:
        f.write(f"{d}\n")