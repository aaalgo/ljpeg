#!/usr/bin/env python
import os
import sys
import re
import subprocess
import numpy

BIN = os.path.join(os.path.dirname(__file__), "jpegdir", "jpeg")

# sample output
#> GW:1979  GH:4349  R:0
#>> C:1  N:xx.ljpeg.1  W:1979  H:4349  hf:1  vf:1

PATTERN = re.compile('\sC:(\d+)\s+N:(\S+)\s+W:(\d+)\s+H:(\d+)\s')

def read (path):
    cmd = '%s -d -s %s' % (BIN, path)
    l = subprocess.check_output(cmd, shell=True)
    #print l
    m = re.search(PATTERN, l)
    C = int(m.group(1)) # I suppose this is # channels
    F = m.group(2)
    W = int(m.group(3))
    H = int(m.group(4))
    assert C == 1
    im = numpy.fromfile(F, dtype='uint16').reshape(H, W)
    L = im >> 8
    H = im & 0xFF
    im = (H << 8) | L
    os.remove(F)
    return im

if __name__ == '__main__':
    x = read('xx.ljpeg').astype('float')
    import cv2
    x = cv2.resize(x, None, None, 0.2, 0.2)
    x = numpy.minimum(x / 256, 255)
    cv2.imwrite("x.jpg", x)



