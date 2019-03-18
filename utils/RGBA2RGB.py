from PIL import Image
import glob, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--src_img_dir", default='data/pokedex-images', help="The directory of source images")
parser.add_argument("--pro_img_dir", default='data/pokedex-images-rgb', help="The directory of processed images")

args = parser.parse_args()

if not os.path.exists(args.pro_img_dir):
    os.mkdir(args.pro_img_dir)
    print("Directory " , args.pro_img_dir ,  " Created ")

for infile in glob.glob(args.src_img_dir + "/*.png"):
    file, ext = os.path.splitext(infile)
    file_name = file.split('/')[-1]
    im = Image.open(infile)
    im = im.convert('RGB')
    im.save(args.pro_img_dir + '/' + file_name + ".png", "PNG")
print("Finished")






# from PIL import Image
# import os, glob
# src = "../data/evol_pairs_supermini"
# dst = "../data/evol_pairs_supermini_rgb"

# for infile in glob.glob(dst + "/*.png"):
#     file, ext = os.path.splitext(infile)
#     file_name = file.split('/')[-1]
#     png = Image.open(infile)
#     print(png.mode)
#     if png.mode == 'RGBA':
#         png.load() # required for png.split()
#         background = Image.new("RGB", png.size, (0,0,0))
#         background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
#         background.save(os.path.join(dst,file_name + '.png'), 'PNG')
    # else:
    #     png.convert('RGB')
    #     png.save(os.path.join(dst,each.split('.')[0] + '.jpg'), 'JPEG')