from forkcocowin import coco_decode, coco_encode
import matplotlib.pyplot as plt

# ----------------------------------------
rlemask = {'size': [50,70], 'counts': '0g05b08J4M2N2NA^O1`0OCO=0E090H080IO68DH;>@C>a0_O_O`0j0OWOF<:CM72I24NL43JM92FN;1ENKO72L0LO91J0MO92INO0NO122OO0M031O000NO31OO11MO40N011MO41MO21L06OL021L06OL021L06OL021L060J040L060J040L060J040L060J040L060J040L060J040L060KO31L060KO31L06OL021L06OL021L06OL021MO41MO21MO40N100NO310O00M0310O00NO1220NO92IONO91KOMO72M0<1EO:2GN63KM34OLM73JF<;=1G_O_Ob0=AC`07EH=1IO71H090F0:1DO>1_O1b0>2N2N3L6H]O'}
print(rlemask)
# ----------------------------------------
mask = coco_decode(rlemask)
# ----------------------------------------
encoded = coco_encode(mask)
print("\nSOURCE")
print(rlemask)
# ----------------------------------------
print("\nENCODED")
print(encoded)
# ----------------------------------------
plt.imshow(mask)
plt.show()


