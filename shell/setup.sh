#!/bin/bash

# create conda env
conda create -n mask python==3.10
conda activate mask

# install torch
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia

# install requirements
pip install -r requirements.txt

# download datasets
gdown 1XDIdwYwNwgK2TF5f9EdW7F2tU077dzau
tar -zxvf dataset.tar.gz && rm dataset.tar.gz

# download ckpts
cd checkpoints
bash -i download_ckpts.sh
cd ..