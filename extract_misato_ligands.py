# import MDAnalysis as mda
# # from MDAnalysis.topology import guess_topology
# # from MDAnalysis.coordinates import PDBWriter
# # from MDAnalysis.lib.util import gro_widths

# # Define the input PDB and output SDF file names
# input_pdb = "misato/1A4G_frames/1A4G_complex_frame_0.pdb"
# output_sdf = "1A4G_ligand_frame_0.sdf"

# # Load the PDB file using MDAnalysis
# u = mda.Universe(input_pdb, format="PDB")

# # Identify the ligand by its residue name (e.g., "LIG")
# ligand_residue_name = "MOL"

# # Create an empty SDF file for writing
# with mda.Writer(output_sdf) as W:
#     # Loop through the frames in the PDB file
#     for ts in u.trajectory:
#         # Select the ligand atoms based on the residue name
#         ligand_atoms = u.select_atoms(f"resname {ligand_residue_name}")
#         if ligand_atoms:
#             # Write the ligand coordinates to the SDF file
#             W.write(ligand_atoms)

# # Clean up and close the SDF file
# writer.close()
# print (f"Ligand extracted and saved to {output_sdf}")


import openbabel

# Define the input PDB and output SDF file names
input_pdb = "misato/1A4G_frames/1A4G_complex_frame_0.pdb"
output_sdf = "misato/1A4G_results/1A4G_ligand_frame_0.sdf"

# Open the PDB file using Pybel
mol_supplier = openbabel.readfile("pdb", input_pdb)

# Initialize an SDF file writer
sdf_writer = openbabel.Outputfile("sdf", output_sdf, overwrite=True)

# Loop through the molecules in the PDB file and find the ligand
for mol in mol_supplier:
    # Identify the ligand molecule (you may need to adjust this based on your PDB format)
    # You can use the residue name or other criteria to identify the ligand.
    # For example, if the ligand has "LIG" as the residue name:
    if mol.data["RESIDUE"] == "MOL":
        # Write the ligand molecule to the SDF file
        sdf_writer.write(mol)

# Close the SDF file writer
sdf_writer.close()
