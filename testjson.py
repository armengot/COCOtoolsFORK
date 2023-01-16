from forkcocowin import coco_decode, coco_encode
import matplotlib.pyplot as plt
from pycocotools.mask import decode, encode
import json
import numpy as np

jfile = "sample.json"
with open(jfile) as J:
    detections = json.load(J)

MYMASK = np.zeros((1040,1388)).astype(np.uint8)
ENMASK = np.zeros((1040,1388)).astype(np.uint8)
PYMASK = np.zeros((1040,1388)).astype(np.uint8)
RGB = np.zeros((1040,1388,3)).astype(np.uint8)
for detmask in detections:
    det = detmask["mask"]
    print("ORIGINAL JSON")
    print("    |   |    ")
    print("    |   |    ")
    print("   -     -   ")
    print("    \   /    ")
    print("     \ /     ")
    print("      ·      ")
    print(det)

    # THIS FORK VERSION DECODE
    mymask = coco_decode(det)
    print(mymask.dtype)
    
    # PYCOCOTOOLS VERSION DECODE
    det["counts"] = bytes(det["counts"],"utf-8")
    pymask = decode(det)
    print(pymask.dtype)
    MYMASK[mymask==1] = 255
    PYMASK[pymask==1] = 255

    # THIS FORK VERSION ENCODE
    myenc = coco_encode(mymask)
    print("MY ENCODE")
    print("    |   |    ")
    print("    |   |    ")
    print("   -     -   ")
    print("    \   /    ")
    print("     \ /     ")
    print("      ·      ")
    print(myenc)
    #mask = coco_decode(myenc)
    #ENMASK[mask==1] = 255

RGB[:,:,0] = MYMASK
RGB[:,:,2] = PYMASK
#RGB[:,:,1] = ENMASK
_,tv = plt.subplots()
tv.imshow(RGB)
tv.set_xticks([])
tv.set_yticks([])
plt.show()

