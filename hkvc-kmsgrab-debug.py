#!/usr/bin/env python3
# KMSGrab external format_modifier, as I am unable to get ffmpeg to do it.
# v20200624IST0047, HanishKVC
#

import os
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image


CMD_CAPTURE="sudo ffmpeg -loglevel debug -f kmsgrab -device /dev/dri/card0 -format_modifier 0x0300000000000013 -i - -vf 'hwdownload,format=bgr0' -t 0.2 -f image2 test%03d.png"

os.system(CMD_CAPTURE)

HSET=128
VSET=8

p=PIL.Image.open("test001.png")
t=p.getdata()
a=np.array(p)
a=np.array(t)
b = a.sum(axis=1)/3
tRows=int(b.shape[0]/HSET)
tCols=int(p.height/VSET)
b10=b.reshape(tRows,HSET)

#plt.matshow(b10[0:400,:])
#plt.show()

nHSets = int(1920/HSET)
rowContinue = nHSets*VSET
c=np.zeros((tCols*VSET,nHSets*HSET))
for y in range(0,tCols):
  for x in range(0,nHSets):
    i= (y*rowContinue)+x*VSET
    j= y*VSET
    print(x,y,i,j)
    if (i >= tRows):
      continue
    c[j:j+VSET,x*HSET:x*HSET+HSET]=b10[i:i+VSET,:]

plt.matshow(c)
plt.show()
