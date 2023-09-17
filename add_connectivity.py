import MDAnalysis as mda
import os, subprocess

PATH = "analysis_combined_pdbs/"

for pdb in os.listdir(PATH):
    pdb_path = PATH + pdb
    for frame_file in os.listdir(pdb_path):
        pdb_file_name = frame_file[:-4]
        frame_uni = mda.Universe(pdb_path + "/" + frame_file, format="PDB")
        guessed_bonds = mda.topology.guessers.guess_bonds(frame_uni.atoms, frame_uni.atoms.positions)
        frame_uni.add_TopologyAttr('bonds', guessed_bonds)
        n_atoms = frame_uni.atoms

        print (pdb_path + "/" + pdb_file_name + "_bonds.pdb")

        # with PDBWriter(f"{pdb_path + "/" + frame_file}_bonds.pdb", n_atoms=n_atoms, bonds='conect') as W:
        #     W.write(frame_uni)