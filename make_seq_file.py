import os
import sys
import os.path as op
from shutil import copyfile

seq_name = sys.argv[0]

####
max_num = 50
file_path = f'/home/user/datasets/arctic_hold/images/{seq_name}'
####

save_path = op.normpath(op.join(file_path, f'../{seq_name}_splited_{max_num}/images'))
files = sorted(os.listdir(file_path))

for i, file_idx in enumerate(range(0, len(files)-1, max_num)):
    tgt = op.join(save_path, f'seq_{i}'); os.makedirs(tgt, exist_ok=True)
    for file in files[file_idx : file_idx+max_num]:
        copyfile(op.join(file_path, file), op.join(tgt, file))