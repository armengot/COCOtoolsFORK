from forkcocowin import coco_decode, coco_encode
import matplotlib.pyplot as plt
from pycocotools.mask import decode, encode
import json
import numpy as np
import time

jfile = "r2d2.json"
with open(jfile) as J:
    detections = json.load(J)

MYMASK = np.zeros((1080,1920)).astype(np.uint8)
ENMASK = np.zeros((1080,1920)).astype(np.uint8)
PYMASK = np.zeros((1080,1920)).astype(np.uint8)
RGB = np.zeros((1080,1920,3)).astype(np.uint8)
for det in detections:
    print(" ================================================================================================ ")
    print(" ================================================================================================ ")
    print(" ================================================================================================ ")
    print("  ORIGINAL JSON")
    print("    |   |    ")
    print("    |   |    ")
    print("   -     -   ")
    print("    \   /    ")
    print("     \ /     ")
    print("      ·      ")
    print(det)

    # THIS FORK VERSION DECODE
    mymask = coco_decode(det)

    
    # PYCOCOTOOLS VERSION DECODE
    det["counts"] = bytes(det["counts"],"utf-8")
    ts = time.time()
    pymask = decode(det)
    te = time.time()
    print("\t"+str(te-ts)+"s encoding")
    MYMASK[mymask==1] = 255
    PYMASK[pymask==1] = 255

    # THIS FORK VERSION ENCODE
    ts = time.time()
    myenc = coco_encode(mymask)
    te = time.time()
    print("\t"+str(te-ts)+"s encoding")
    print("  MY ENCODE")
    print("    |   |    ")
    print("    |   |    ")
    print("   -     -   ")
    print("    \   /    ")
    print("     \ /     ")
    print("      ·      ")
    print(myenc)
    print(" ------------------------------------------------------------------------------------------------")
    #mask = coco_decode(myenc)
    #ENMASK[mask==1] = 255

RGB[:,:,0] = MYMASK
RGB[:,:,1] = MYMASK
RGB[:,:,2] = MYMASK
#RGB[:,:,1] = PYMASK
_,tv = plt.subplots()
tv.imshow(RGB)
tv.set_xticks([])
tv.set_yticks([])
plt.show()
