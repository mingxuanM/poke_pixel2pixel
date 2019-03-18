from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--img_path", default='data/pokemon-images/1.png', help="The path of image")
args = parser.parse_args()
image = Image.open(args.img_path)
print(image.mode)




