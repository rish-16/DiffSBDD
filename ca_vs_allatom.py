import os, subprocess, re
import MDAnalysis as mda
from MDAnalysis.analysis import align, rms
import numpy as np

"""
for Calpha and AA models:
    - for a given PDB, get each frame, 
    - generate 100 ligands per frame
    - compute average number of steric clashes
    - plot for each frame
"""

PATH_2I3I = "test_analysis/combined_2I3I/"
PATH_contents = os.listdir(PATH_2I3I)

# if not os.path.exists("cg_results/"):

for pdb_fn in PATH_contents:
    if "_bonds" in pdb_fn:
        fp = PATH_2I3I + pdb_fn
        frame_idx = re.findall(r'\d+', pdb_fn)[-1]
        # test_analysis/combined_2I3I/2I3I_MD_frame0.pdb_bonds.pdb
        pdb_name = pdb_fn.split(".")[0][:4]

        # python generate_ligands.py ckpt/moad_ca_cond.ckpt --pdbfile analysis_combined_pdbs/combined_1MFI/1MFI_MD_frame82.pdb --outdir analysis_output/1MFI_frame82_result/ --ref_ligand B:344
        print (f"# {pdb_fn} frame {frame_idx}")
        print (f"python generate_ligands.py ckpt/moad_ca_cond.ckpt --pdbfile  analysis_combined_pdbs/combined_{pdb_name}/{pdb_fn} --outdir cg_results/{pdb_name}_results_ca/ --ref_ligand X:92")
