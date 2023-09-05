from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem.Fingerprints import FingerprintMols
import numpy as np
import matplotlib.pyplot as plt
import os, re

sdf_path = "1CNX_results/"
sdf_dir = os.listdir(sdf_path)
sdf_dir = list(sorted(sdf_dir))

all_mols = [
    Chem.MolFromMolFile('1cnx_ligand_gt.sdf')
]

for path in sdf_dir:
    fp = sdf_path + path
    mol = Chem.MolFromMolFile(fp)
    all_mols.append(mol)

table = [[0 for _ in range(len(all_mols))] for _ in range(len(all_mols))]

for i, mi in enumerate(all_mols):
    fpi = FingerprintMols.FingerprintMol(mi)
    for j, mj in enumerate(all_mols):
        if i != j:
            fpj = FingerprintMols.FingerprintMol(mj)
            tan = DataStructs.TanimotoSimilarity(fpi, fpj)
            table[i][j] = tan

table = np.array(table)            
print (table.shape)

plt.imshow(table, cmap='viridis')
# plt.grid(True)
plt.colorbar(label=r'Tanimoto Similarity')
plt.title("ID: 1CNX")
plt.xticks(ticks=range(len(all_mols)), labels=['GT Ligand'] + ['Frame ' + str(re.findall(r"\d+", f)[1]) for f in sdf_dir], rotation=90, fontsize=12)
plt.yticks(ticks=range(len(all_mols)), labels=['GT Ligand'] + ['Frame ' + str(re.findall(r"\d+", f)[1]) for f in sdf_dir], rotation=0, fontsize=12)
# plt.xlabel('Ligand', fontdict={'size': 17})
# plt.ylabel('Ligand', fontdict={'size': 17})
print (sdf_dir[1 + 6])
plt.tight_layout()
plt.show()