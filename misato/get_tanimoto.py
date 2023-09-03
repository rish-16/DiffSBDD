from rdkit import Chem, DataStructs
from rdkit.Chem import PandasTools
from rdkit.Chem import AllChem
import numpy as np
import matplotlib.pyplot as plt
import os

# ref = Chem.MolFromSmiles('Nc1nc2nc(N)nc(N)c2nc1-c1cccc(Cl)c1')
# fp1 = Chem.RDKFingerprint(ref)

sdf_path = "1CNX_results/"
sdf_dir = os.listdir(sdf_path)

# suppl = Chem.SDMolSupplier('yourSDF.sdf')

all_mols = []

for path in sdf_dir:
    fp = sdf_path + path
    mol = PandasTools.LoadSDF(fp)
    all_mols.append(mol)

fpgen = AllChem.GetRDKitFPGenerator(fpSize=1024,maxPath=2)

table = [[0 for _ in range(len(all_mols))] for _ in range(len(all_mols))]
for i, mi in enumerate(all_mols):
    print (mi)
    fpi = fpgen.GetFingerprint(mi)
    for j, mj in enumerate(all_mols):
        if i != j:
            fpj = fpgen.GetFingerprint(mj)
            tan = DataStructs.TanimotoSimilarity(fpi, fpj)
            table[i][j] = tan

table = np.array(table)            
print (table.shape)

plt.imshow(table, cmap='viridis')
plt.xlabel('Molecule')
plt.ylabel('Molecule')
plt.colorbar(label=r'Tanimoto Similarity')
plt.show()            