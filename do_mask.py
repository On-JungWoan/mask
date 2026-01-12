import os
import cv2
import argparse
import numpy as np
import os.path as op
from PIL import Image
from glob import glob

def main(args):
    root_res_dir = op.join(os.getcwd(), 'results', args.img_name, 'npy/*.npy')
    root_ipt_dir = op.join(os.getcwd(), 'inputs', args.img_name, '*.jpg')
    save_dir = op.join(args.output_path, args.img_name)
    os.makedirs(save_dir, exist_ok=True)
    
    #! load mask
    masks = np.concatenate([np.load(p)[None] for p in sorted(glob(root_res_dir))])
    
    #! load img
    img_names = sorted(glob(root_ipt_dir))
    imgs = np.concatenate([np.array(Image.open(p))[None] for p in img_names])

    assert masks.shape[0] == imgs.shape[0]
    
    for idx in range(len(masks)):
        img_name = img_names[idx].split('/')[-1]
        mask = masks[idx]
        img = imgs[idx]
        
        cv2.imwrite(f'{save_dir}/{img_name}', (img * mask[..., None])[..., ::-1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--img_name", type=str, required=True)
    parser.add_argument("--output_path", type=str, default='results/0_masked_output')
    args = parser.parse_known_args()[0]
    
    main(args)