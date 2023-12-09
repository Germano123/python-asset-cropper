import cv2
import os

img_path = "./example.png"

img = cv2.imread(img_path)

M = 32
N = 32

tiles = [img[x:x+M,y:y+N] for x in range(0,img.shape[0],M) for y in range(0,img.shape[1],N)]

current_dir = os.getcwd()

count = 0
for tile in tiles:
    count += 1
    asset_name = current_dir+f"\\new_asset\\asset_{count}.png"
    # print(asset_name)
    cv2.imwrite(asset_name, tile)

