import numpy as np
import ctypes

'''
    COCO API encode/decode functions
    re-written by Marcelo Armengot (C) 2022

    and is available from: https://github.com/armengot/COCOtoolsFORK
    as derived from C version: https://github.com/cocodataset/cocoapi
    see legacy license: https://github.com/cocodataset/cocoapi/blob/master/license.txt
'''

def coco_decode(rlemask):
    masksize = rlemask["size"]
    h = masksize[0]
    w = masksize[1]

    # rleFrString() translation
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
    
    # rleDecode() translation
    i = 0
    N = m.value
    M = np.zeros(w*h).astype(np.byte)
    j = 0
    i = 0
    v = ctypes.c_byte(0)
    while j<N:
        k = 0
        # optimization update
        M[i:i+cnts[j]] = v.value * np.ones(cnts[j]).astype(np.byte)
        k = k + cnts[j]
        i = i + cnts[j]
        '''
        # previous equivalent (but slower)
        while k<cnts[j]:
            M[i] = v.value
            k = k + 1
            i = i + 1
        '''
        v.value = not v.value
        j = j + 1
    output = np.reshape(M,(w,h)).astype(np.byte)
    return(output.transpose().astype(np.uint8))

def coco_encode(mask):
    w = mask.shape[0]
    h = mask.shape[1]

    # rleEncode() translation
    a = w*h
    cnts = np.zeros(a+1).astype(np.uint32)
    M = np.zeros(w*h).astype(np.byte)
    M = np.ravel(mask.transpose())
    j = 0
    k = 0
    p = ctypes.c_byte(0)
    c = ctypes.c_uint32(0)
    while j<a:
        if (M[j]!=p.value):
            cnts[k] = c.value
            k = k + 1
            c.value = 0
            p.value = M[j]
        c.value = c.value + 1
        j = j + 1    
    cnts[k] = c.value

    # rleToString() translation
    i = 0
    m = ctypes.c_ulong(k+1)
    x = ctypes.c_long(0)
    c = ctypes.c_byte(0)
    s = ""
    while i<m.value:
        x = ctypes.c_long(cnts[i])
        if (x.value>2):
            x.value = x.value - ctypes.c_long(cnts[i-2]).value
        more = 1
        while (more):
            c = ctypes.c_byte(x.value & (0x1f))
            x.value >>= 5
            if (c.value & ctypes.c_byte(0x10).value):
                more = x.value!=-1
            else:
                more = x.value!=0
            if (more):
                c.value |= 0x20
            c.value = c.value + 48
            s = s + chr(c.value)
        i = i + 1
    js = {'size':[w,h], 'counts': s}
    return(js)