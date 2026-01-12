import os
import shutil
from PIL import Image
from glob import glob

tgt_dirs = sorted(glob('inputs/*'))

#! for the making folder
tgt_dir = [d for d in tgt_dirs if '.' in d]
for d in tgt_dir:
    seq_name = d.split('/')[-1].split('.')[0]
    new_dir = f'inputs/{seq_name}'
    
    os.makedirs(new_dir, exist_ok=True)
    shutil.move(d, new_dir)


#! for the resizing
tgt_dir = [d for d in tgt_dirs if ('_' not in d) and ('backup' not in d)]
for d in tgt_dir:
    _ = glob(f'{d}/*'); assert len(_) == 1
    seq_name = d.split('/')[-1].split('.')[0]
    
    img = Image.open(_[0])
    resized_img = img.resize([1024, 1024])
    
    shutil.move(d, f'inputs/backup/{seq_name}')
    os.makedirs(d, exist_ok=True)
    resized_img.save(_[0])