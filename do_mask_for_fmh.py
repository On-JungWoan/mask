import os
import cv2
import argparse
import numpy as np
import os.path as op
from PIL import Image
from glob import glob

def main(args):
    save_dir = f"../../output/{args.img_name}/mask"
    os.makedirs(save_dir, exist_ok=True)    
    
    root_res_dirs = op.join(os.getcwd(), 'results', args.img_name, '*')
    root_ipt_dir = op.join(os.getcwd(), 'inputs', args.img_name, '*.jpg')
    
    
    #! mask collection
    mask_dict = {}
    for root_res_dir in glob(root_res_dirs):
        _type = root_res_dir.split('/')[-1]
        mask = np.concatenate([np.load(p)[None] for p in sorted(glob(f'{root_res_dir}/npy/*'))])
        
        mask_dict[_type] = mask
    mask_dict['hoi'] = sum(mask_dict.values())
    

    #! load img
    img_names = sorted(glob(root_ipt_dir))
    imgs = np.concatenate([np.array(Image.open(p))[None] for p in img_names])
    img = imgs[0]
    
    
    #! do mask
    for _type, mask in mask_dict.items():
        res_img = (img * mask[..., None])[..., ::-1]
        res_img = np.concatenate([res_img, mask[..., None]*255.], axis=-1)[0]
        cv2.imwrite(f'{save_dir}/{_type}.png', res_img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--img_name", type=str, required=True)
    args = parser.parse_known_args()[0]
    
    main(args)