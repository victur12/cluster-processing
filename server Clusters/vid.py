import cv2
import numpy as np
import glob

frameSize = (426, 240)

out = cv2.VideoWriter('videoBlancoNegro.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, frameSize)

for filename in glob.glob('*.jpg'):
    img = cv2.imread(filename)
    out.write(img)

out.release()