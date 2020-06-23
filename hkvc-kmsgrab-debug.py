#!/usr/bin/env python3
# Experiment with ffmpeg KMSGrab
# v20200623IST1750, HanishKVC
#

import os

CMD_CAPTURE="sudo ffmpeg -loglevel debug -f kmsgrab -device /dev/dri/card0 -format_modifier 0x0300000000000013 -i - -vf 'hwdownload,format=bgr0' -t 0.2 -f image2 test%03d.png"

os.system(CMD_CAPTURE)

