#!/usr/bin/env python3
# KMSGrab external format_modifier, as I am unable to get ffmpeg to do it.
# v20200624IST0024, HanishKVC
#

import os
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image


CMD_CAPTURE="sudo ffmpeg -loglevel debug -f kmsgrab -device /dev/dri/card0 -format_modifier 0x0300000000000013 -i - -vf 'hwdownload,format=bgr0' -t 0.2 -f image2 test%03d.png"

os.system(CMD_CAPTURE)


p=PIL.Image.open("test001.png")
t=p.getdata()
a=np.array(p)
a=np.array(t)
b = a.sum(axis=1)/3
1920*1080/128
b10=b.reshape(16200,128)

plt.matshow(b10[0:400,:])
plt.show()

1920/128
15*8
c=np.zeros((1024,128))
for y in range(1,100):
  i= y*120
  j= y*8
  print(y,i,j)
  c[j:j+8,:]=b10[i:i+8,:]
plt.matshow(c)
plt.show()
