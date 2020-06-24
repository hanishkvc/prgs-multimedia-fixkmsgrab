#!/usr/bin/env python3
# KMSGrab external format_modifier, as I am unable to get ffmpeg to do it.
# v20200624IST1123, HanishKVC
#

import os
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image


bFullSet=True
HSET=128
VSET=8


CMD_CAPTURE="sudo ffmpeg -loglevel debug -f kmsgrab -device /dev/dri/card0 -format_modifier 0x0300000000000013 -i - -vf 'hwdownload,format=bgr0' -t 0.2 -f image2 test%03d.png"
os.system(CMD_CAPTURE)


p=PIL.Image.open("test001.png")
WIDTH=p.width
HEIGHT=p.height


t=p.getdata()
a=np.array(p)
a=np.array(t)
b = a.sum(axis=1)/3
tRows=int(b.shape[0]/HSET)
tCols=int(p.height/VSET)
b10=b.reshape(tRows,HSET)


nHSets = int(WIDTH/HSET)
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


if bFullSet:
  pltRows = 2
  pltCols = 2
  fh = 20
  fw = fh
  fh += 1
else:
  pltRows = 1
  pltCols = 2
  ar = WIDTH*pltCols/HEIGHT
  fh = 10
  fw = int(fh*ar+1)
fig,ax = plt.subplots(pltRows, pltCols, figsize=(fw,fh))
fig.axes[0].matshow(b.reshape(HEIGHT,WIDTH))
fig.axes[1].matshow(c)
if bFullSet:
  fig.axes[2].imshow(p)
  fig.axes[3].matshow(b10[0:int(tRows*0.03),:])
plt.tight_layout(True)
plt.savefig("compare_fixkmsgrab.png")
plt.show()

