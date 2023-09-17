import os, subprocess

PATH = "/data/rishabh/BindingMOAD_2020/"

for file in os.listdir(PATH):
    if "bio1" in file:
        fp = PATH + file
        new_fp = file[:-5]
        cmd = f"mv {fp} {PATH + new_fp}_1.pdb"
        subprocess.call(cmd, shell=True)
    elif "bio2" in file:
        fp = PATH + file
        new_fp = file[:-5]
        cmd = f"mv {fp} {PATH + new_fp}_2.pdb"
        subprocess.call(cmd, shell=True)
    else:
        print (file)