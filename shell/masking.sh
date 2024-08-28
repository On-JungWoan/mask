#!/bin/bash

seq_name='arctic_s03_box_grab_01_1'

# activate venv
conda activate mask

# run server
python segment_anything_2/mask_app.py --root_dir dataset/$seq_name