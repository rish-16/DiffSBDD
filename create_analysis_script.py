import os, re, subprocess, json, csv
import MDAnalysis as mda
from MDAnalysis.analysis import align

PDB_PATH = "analysis_combined_pdbs/"
all_pdb_dirs = os.listdir(PDB_PATH)

for pdb_dir in all_pdb_dirs:
    frames_path = os.listdir(PDB_PATH + pdb_dir)
    pdb_universes = []
    for frame_path in frames_path:
        frame_pdb = mda.Universe(frame_path)
        frame_id = frame_id[:-4]
        frame_id = frame_path.split("_")[-1].replace("frame", "").strip()
        print (pdb_dir, frame_pdb, frame_id)
        # print (f"python generate_ligands.py ckpt/moad_ca_cond.ckpt --pdbfile {PDB_PATH + pdb_dir + "/" + frame_path} --outdir analysis_output/{}/")