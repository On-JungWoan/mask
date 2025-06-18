import os
import shutil
import argparse
import os.path as op
from PIL import Image

def main(args):
    root_dir = args.root_dir
    backup_dir = op.join(root_dir, '../backup')
    seq_name = root_dir.split('/')[-1]
    
    #* bu
    shutil.move(root_dir, backup_dir)
    
    #* mkdir
    os.makedirs(backup_dir, exist_ok=True)
    os.makedirs(root_dir, exist_ok=True)
    
    tgt_dir = op.join(backup_dir, seq_name)
    for img_name in sorted(os.listdir(tgt_dir)):
        img = Image.open(op.join(tgt_dir, img_name))
        img.save(op.join(root_dir, img_name).replace('png', 'jpg'))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--root_dir", type=str, default='/home/user/ojw/BIGS_release/ml-hugs/preprocess/mask/inputs/custom')
    
    args = parser.parse_args()
    
    root = op.join(os.getcwd(), 'inputs')
    all_path = [op.join(root, d) for d in os.listdir('inputs') if d != '_' and d != 'backup' and d != 'videos']
    for p in all_path:
        args.root_dir = p
        main(args)