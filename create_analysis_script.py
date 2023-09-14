import os, re, subprocess, json, csv
from pprint import pprint
import MDAnalysis as mda
from MDAnalysis.analysis import align

PDB_PATH = "analysis_combined_pdbs/"
all_pdb_dirs = os.listdir(PDB_PATH)

with open("PDB_IDs/misato_moad_pocket_info.txt", "r") as f:
    moad_pocket_info_records = f.read().strip().split()
    moad_pocket_info_records = [d.strip().split(",") for d in moad_pocket_info_records]

moad_pocket_info_records = {
    rec[0] : rec[-1]
    for rec in moad_pocket_info_records
}

print (len(moad_pocket_info_records))

for pdb_dir in all_pdb_dirs:
    frames_path = os.listdir(PDB_PATH + pdb_dir)
    pdb_universes = []
    for frame_path in frames_path:
        print (PDB_PATH + pdb_dir + "/" + frame_path)
        frame_pdb = mda.Universe(PDB_PATH + pdb_dir + "/" + frame_path, format="PDB")
        frame_id = frame_path[:-4]
        frame_id = frame_id.split("_")[-1].replace("frame", "").strip()
        pdb_name = frame_path[:4]
        chain_info = moad_pocket_info_records[pdb_name]

        final_path = PDB_PATH + pdb_dir + "/" + frame_path
        print (f"python generate_ligands.py ckpt/moad_ca_cond.ckpt --pdbfile {final_path} --outdir analysis_output/{pdb_name}_frame{frame_id}_result/ --ref_ligand {chain_info}")