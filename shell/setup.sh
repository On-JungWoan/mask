#!/bin/bash

# create conda env
conda create -n mask python==3.10
conda activate mask

# install torch
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# install requirements
pip install -e segment_anything_2
pip install -r requirements.txt

# download ckpts
cd checkpoints
bash -i download_ckpts.sh
cd ..