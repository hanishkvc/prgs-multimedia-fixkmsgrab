===============================
UnTile ffmpeg kmsgrab output
===============================
Author: HanishKVC
Version: v20200624IST1234


Noticed that kmsgrab hwdownload output is not linear, rather its a tiled image data, and for some reason passing format_modifier option to ffmpeg doesnt seem to be helping, or I am passing it wrongly. So had to scratch my itch ;-)

Either way as I wanted to check something, created this simple python script to untile the output and recover the required rough image, monochromatic for now.

This is a simple flow to try and just to explore how things may be tiled and inturn try and untile it. Currently it handles the untiling for the way the image data is tiled in one of my machines.

Some References
-----------------

drm_fourcc.h

kmsgrab.c

