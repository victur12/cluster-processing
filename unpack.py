import shutil
import glob
import numpy as np
import cv2

for filename in glob.glob('*.zip'):
    shutil.unpack_archive(filename)
    