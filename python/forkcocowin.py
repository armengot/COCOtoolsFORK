import numpy as np
import ctypes

def coco_decode(rlemask):
    masksize = rlemask["size"]
    h = masksize[0]
    w = masksize[1]
    mstring = rlemask["counts"]
    m = len(mstring) #np.uint(len(mstring))
    cnts = np.zeros(m).astype(np.uint32)
    x = ctypes.c_ulong(0)
    p = ctypes.c_ulong(0)
    m = ctypes.c_ulong(0)
    k = ctypes.c_ulong(0)
    N = ctypes.c_ulong(len(mstring))
    while p.value<N.value:
        more = 1
        x = ctypes.c_ulong(0)
        k = ctypes.c_ulong(0)
        while more:
            c = ord(mstring[p.value]) - 48
            x.value |= (c & 0x1f) << 5*k.value
            more = c & 0x20
            p.value = p.value + 1
            k.value = k.value + 1
            if (not more)and(c & 0x10):
                x.value |= -1 << 5*k.value
        if (m.value>2):
            aux = cnts[m.value-2]
            x.value = x.value + aux
        cnts[m.value]=ctypes.c_uint32(x.value).value
        m = ctypes.c_ulong(m.value + 1)
    i = 0
    N = m.value
    M = np.zeros(w*h).astype(np.byte)
    j = 0
    i = 0
    v = ctypes.c_byte(0)
    while j<N:
        k = 0
        while k<cnts[j]:
            M[i] = v.value
            k = k + 1
            i = i + 1
        v.value = not v.value
        j = j + 1
    output = np.reshape(M,(w,h)).astype(np.byte)
    return(output.transpose())