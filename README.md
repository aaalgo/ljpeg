Usage:

0. Install flex with
``` apt-get install flex```.
Building without flex will fail and pollute the codebase.

1. In your python project
	```
	git clone https://github.com/aaalgo/ljpeg.git

	```
	Or if you are using git already:
	```
	git submodule add https://github.com/aaalgo/ljpeg.git

	```
2. Produce the jpeg binary.
	```
	cd jpegdir; make

	```
3. In your python code:
	```
	from ljpeg import ljpeg

	x = ljpeg.read(path)
	```

	The loaded is a matrix of type uint16.  Typically you want to convert that
	to float for subsequent processing.
	```
	x = ljpeg.read(path).astype('float')
	```

	The LJPEG format sometimes has wrong values for width and height (transposed).
	One has to read the correct values of width and height from the associating .ics file.
	Below is a sample snippet for this purpose:
	```
	    W = None
	    H = None
	    # find the shape of image
	    for l in open(ics, 'r'):
		l = l.strip().split(' ')
		if len(l) < 7:
		    continue
		if l[0] == name:
		    W = int(l[4])
		    H = int(l[2])
		    bps = int(l[6])
		    if bps != 12:
			logging.warn('BPS != 12: %s' % path)
		    break

	    assert W != None
	    assert H != None

	    if W != image.shape[1]:
		logging.warn('reshape: %s' % path)
		image = image.reshape((H, W))
	```

4. Using ljpeg.py standalone:
	- Convert to TIFF (requires the .ics file in the same directory as LJPEG)
	```
	./ljpeg.py cases/benigns/benign_01/case0029/C_0029_1.LEFT_CC.LJPEG output.tiff
	```
	- Convert to TIFF and verify that no information has been lost
	```
	./ljpeg.py cases/benigns/benign_01/case0029/C_0029_1.LEFT_CC.LJPEG output.tiff --verify
	```
	- Convert to jpeg for visualization with down-sizing scale=0.3 (16-bit TIFF is not good for direct visualization)
	```
	./ljpeg.py cases/benigns/benign_01/case0029/C_0029_1.LEFT_CC.LJPEG output.jpg --visual --scale 0.3
	```
	Note that output file can be any format that's supported by OpenCV (which includes all common types).  Most file formats only support 8-bit images, so directly saving into such file formats will cause problems.  Add "--visual" to normalize color into 8-bit before saving to such file formats.

The Stanford ljpeg code is in public domain and is therefore OK to be
included here.  I did minor modification to make the code compile under
modern Linux.
