import MDAnalysis as mda
from rdkit import Chem
from rdkit.Chem import AllChem

# Define the input PDB and output SDF file names
input_pdb = "misato/1A4G_frames/1A4G_complex_frame_0.pdb"
output_sdf = "misato/1A4G_results/1A4G_ligand_frame_0.sdf"

# Load the PDB file using MDAnalysis
u = mda.Universe(input_pdb, guess_toplogy=True, format="PDB")

# Identify the ligand by its residue name (e.g., "LIG")
ligand_residue_name = "MOL"

# Initialize an RDKit molecule to store the ligand
ligand_molecule = Chem.Mol()

# Loop through the frames in the PDB file
for ts in u.trajectory:
    # Select the ligand atoms based on the residue name
    ligand_atoms = u.select_atoms(f"resname {ligand_residue_name}")
    print (ligand_atoms)

    if ligand_atoms:
        # Convert ligand coordinates to an RDKit molecule
        ligand_block = ligand_atoms.atoms.write("pdb").decode("utf-8")
        ligand_mol_block = Chem.MolFromPDBBlock(ligand_block)

        # Merge the ligand molecule with the existing one
        if ligand_mol_block is not None:
            ligand_molecule = Chem.CombineMols(ligand_molecule, ligand_mol_block)

# Generate a 3D conformer for the ligand
if ligand_molecule is not None:
    ligand_molecule = Chem.AddHs(ligand_molecule)
    AllChem.EmbedMolecule(ligand_molecule, AllChem.ETKDG())

    # Save the ligand molecule to the SDF file
    with Chem.SDWriter(output_sdf) as writer:
        writer.write(ligand_molecule)

print(f"Ligand extracted and saved to {output_sdf}")