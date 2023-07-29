conda create -n sbdd-env
conda activate sbdd-env
conda install pytorch cudatoolkit=10.2 -c pytorch
conda install -c conda-forge pytorch-lightning
conda install -c conda-forge wandb
conda install -c conda-forge rdkit
conda install -c conda-forge biopython
conda install -c conda-forge imageio
conda install -c anaconda scipy
conda install -c pyg pytorch-scatter
conda install -c conda-forge openbabel
