#!/usr/bin/env python3
# Experiment with KMSGrab
# v20200623IST1707, HanishKVC
#

import os

os.system("sudo ffmpeg -loglevel debug -f kmsgrab -device /dev/dri/card0 -i - -vf 'hwdownload,format=bgr0' -t 0.2 -f image2 test%03d.png")

