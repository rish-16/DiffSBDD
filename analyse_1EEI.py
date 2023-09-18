import os, subprocess, re
import MDAnalysis as mda
import numpy as np

PATH = "combined_1EEI/"
pdb_1EE1_dir = os.listdir(PATH)

frame_pocket_sets = {}
for fp in pdb_1EE1_dir:
    if "_bonds" in fp: # only look at files with CONECT bond information inside
        frame_idx = re.findall(r"\d+", fp)[-1]
        print (f"python generate_ligands.py ckpt/moad_ca_cond.ckpt --pdbfile analysis_combined_pdbs/combined_1EEI/{fp} --outdir analysis_results/results_1EEI/frame_{frame_idx}_1EEI/ --ref_ligand X:517")