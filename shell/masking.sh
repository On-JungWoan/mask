#!/bin/bash

seq_name=$1

# activate venv
conda activate mask

# run server
python segment_anything_2/mask_app.py --root_dir dataset/$seq_name