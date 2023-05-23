# -*- coding: utf-8 -*-

import pathlib
import cv2
import numpy as np
import os
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--hl")
parser.add_argument("--sl")
parser.add_argument("--vl")
parser.add_argument("--hh")
parser.add_argument("--sh")
parser.add_argument("--vh")


args = parser.parse_args()

def remove_green_screen(img):
    import cv2
    import numpy as np
    import skimage.exposure

    # convert to LAB
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # extract A channel
    A = lab[:,:,1]

    # threshold A channel
    thresh = cv2.threshold(A, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # blur threshold image
    blur = cv2.GaussianBlur(thresh, (0,0), sigmaX=5, sigmaY=5, borderType = cv2.BORDER_DEFAULT)

    # stretch so that 255 -> 255 and 127.5 -> 0
    mask = skimage.exposure.rescale_intensity(blur, in_range=(127.5,255), out_range=(0,255)).astype(np.uint8)

    # add mask to image as alpha channel
    result = img.copy()
    result = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    result[:,:,3] = mask

    return result







 # mask = cv2.inRange(hsv, (40, 50,50), (86, 255, 255)) #H180 S255 V255 H78~160 Default60:50:50-86:255:255        ksize=15
if args.hl:
    hl = int(args.hl)
else:
    hl = 30
if args.sl:
    sl = int(args.sl)
else:
    sl = 64
if args.vl:
    vl = int(args.vl)
else:
    vl = 0

if args.hh:
    hh = int(args.hh)
else:
    hh = 90
if args.sh:
    sh = int(args.sh)
else:
    sh = 255
if args.vh:
    vh = int(args.vh)
else:
    vh = 255

print("hl:",hl,"_sl:",sl,"_vl:",vl)
print("hh:",hh,"_sh:",sh,"_vh:",vh)


#入力画像ディレクトリ
input_dir_base = "object"
output_dir_base = "trimmed"
category = "."

files = os.listdir(input_dir_base)
files_dir = [f for f in files if os.path.isdir(os.path.join(input_dir_base, f))]
print(files_dir)
print("label=>",len(files_dir))

for j in range(len(files_dir)):
    category = files_dir[j]
    print("category:",category)
    input_dir = input_dir_base + "\\" + category
    # input_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))
    input_list = list(pathlib.Path(input_dir).glob('**/*.png'))
    output_dir = output_dir_base + "\\" + category

    # 出力フォルダにラベルごとのフォルダが存在していなければ作成
    if not os.path.isdir(output_dir):
            print("INFO:出力フォルダに",category,"のフォルダを作成します。")
            os.mkdir(output_dir)
    else:
        print("INFO:出力フォルダには",category,"フォルダがすでに存在しています。")
    
    print("グリーンバック除去開始->",len(input_list))
    for i in range(len(input_list)):
        img_file_name = str(input_list[i])
        print( "IMPORT:",img_file_name )

        ## グリーンバック除去&png出力
        img = cv2.imread( img_file_name , -1)
        img2 = remove_green_screen( img )
        
        file_name = os.path.splitext(os.path.basename(img_file_name))[0]
        output_file_name = output_dir + "\\" + category + str(i).zfill(8) + ".png"
        cv2.imwrite( output_file_name ,img2)
        
        # 画像を読み込む
        image = Image.open( output_file_name )
        # 不要な透明画素を除去
        cropped_image = image.crop(image.getbbox())
        # 画像を保存
        cropped_image.save(output_file_name)

        print("EXPORT:",output_file_name)


