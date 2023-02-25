#!/usr/bin/env python3
import argparse
import glob
import logging
import os
import re
import subprocess
import sys

import cv2
import numpy

BIN = os.path.join(os.path.dirname(__file__), "jpegdir", "jpeg")

if not os.path.exists(BIN):
    print("jpeg is not built yet; use 'cd jpegdir; make' first")
    sys.exit(0)

# sample output
# > GW:1979  GH:4349  R:0
# >> C:1  N:xx.ljpeg.1  W:1979  H:4349  hf:1  vf:1

PATTERN = re.compile(r"\sC:(\d+)\s+N:(\S+)\s+W:(\d+)\s+H:(\d+)\s")


def read(path):
    cmd = "{} -d -s {}".format(BIN, path)
    output = subprocess.check_output(cmd, shell=True)
    # print(output)
    m = re.search(PATTERN, output.decode())
    C = int(m.group(1))  # I suppose this is # channels
    F = m.group(2)
    W = int(m.group(3))
    H = int(m.group(4))
    assert C == 1
    im = numpy.fromfile(F, dtype="uint16").reshape(H, W)
    L = im >> 8
    H = im & 0xFF
    im = (H << 8) | L
    os.remove(F)
    return im


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("ljpeg", nargs=1)
    parser.add_argument("output", nargs=1)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--visual", action="store_true")
    parser.add_argument("--scale", type=float)

    args = parser.parse_args()
    path = args.ljpeg[0]
    tiff = args.output[0]

    assert "LJPEG" in path

    root = os.path.dirname(path)
    print(root)
    stem = os.path.splitext(path)[0]

    # read ICS
    print(glob.glob(root + "/*.ics"))
    ics = glob.glob(root + "/*.ics")[0]
    name = path.split(".")[-2]

    W = None
    H = None
    # find the shape of image
    for line in open(ics, "r"):
        line = line.strip().split(" ")
        if len(line) < 7:
            continue
        if line[0] == name:
            W = int(line[4])
            H = int(line[2])
            bps = int(line[6])
            if bps != 12:
                logging.warning("BPS != 12: %s" % path)
            break

    assert W is not None
    assert H is not None

    image = read(path)

    if W != image.shape[1]:
        logging.warning("reshape: %s" % path)
        image = image.reshape((H, W))

    raw = image

    if args.visual:
        logging.warning("normalizing color, will lose information")
        if args.verify:
            logging.error("verification is going to fail")
        if args.scale:
            rows, cols = image.shape
            image = cv2.resize(image, (int(cols * args.scale), int(rows * args.scale)))
        image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
        image = numpy.uint8(image)
    elif args.scale:
        logging.error("--scale must be used with --visual")
        sys.exit(1)
        # image = cv2.equalizeHist(image)
    # tiff = stem + '.TIFF'
    cv2.imwrite(tiff, image)

    if args.verify:
        verify = cv2.imread(tiff, -1)
        if numpy.all(raw == verify):
            logging.info("Verification successful, conversion is lossless")
        else:
            logging.error("Verification failed: %s" % path)
