import os, subprocess

PATH = "PDB_IDs/misato_moad_og_crystal_structs.txt"

with open(PATH, "r") as f:
    og_crystal_data = f.read().strip().split("\n")[1:] # ignore header
    og_crystal_data = [d.strip().split(",") for d in og_crystal_data]

for rec in og_crystal_data:
    pdb_id = rec[0]
    path = "og_crystal_structs/" + rec[1].split("/")[-1]
    chain_info = rec[2]    

    print (f"python generate_ligands.py ckpt/moad_ca_cond.ckpt --pdbfile {path} --outdir diffsbdd_analysis_results/{pdb_id}_results/ --ref_ligand {chain_info}")

    # python generate_ligands.py ckpt/crossdocked_fullatom_cond.ckpt --pdbfile misato/1CNX_frames/1CNX_complex_frame_0.pdb --outdir misato/1CNX_results/ --ref_ligand X:258