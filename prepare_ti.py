import os
import shutil

seq_name = 'box_grab_01'
input_root = f'inputs/for_mask/{seq_name}'
output_root = f'results/for_mask/{seq_name}'

input_dirs = [f'{input_root}/{c}' for c in sorted(os.listdir(output_root))] #! output_root
output_dirs = [f'{output_root}/{c}' for c in sorted(os.listdir(output_root))]

input_imgs = sum([[f'{d}/{i}' for i in sorted(os.listdir(d))] for d in input_dirs], [])
output_masks = sum([[f'{d}/img/{i}' for i in sorted(os.listdir(f'{d}/img'))] for d in output_dirs], [])
assert len(input_imgs) == len(output_masks)

tgt_path = f'ti/{seq_name}'
tgt_input_path = f'{tgt_path}/input'; os.makedirs(tgt_input_path, exist_ok=True)
tgt_output_path = f'{tgt_path}/output'; os.makedirs(tgt_output_path, exist_ok=True)
for idx in range(len(input_imgs)):
    shutil.copy(input_imgs[idx], f'{tgt_input_path}/{idx:05}.jpg')
    shutil.copy(output_masks[idx], f'{tgt_output_path}/{idx:05}.jpg')