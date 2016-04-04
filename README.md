Usage:

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
	to float for subsequent processing.  Because uint16 has a larger range than
	what can be saved with typical image format like jpeg (for the purpose of
	visualization only), it is also recommended that you divide the loaded image
	by 256.  That is, you can load the image with the following:
	```
	x = ljpeg.read(path).astype('float') / 256
	```
	So the pixel values will all fall within the range of [0, 256).
	Note that dividing a float value by 256 does not cause any precision loss.
	Precision lost only occurs when you save the image to a jpeg file, which typically
	involving convert pixel values to 8-bit unsigned integers.  For lossless
	file storage, use [numpy.savez](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.savez.html).

The Stanford ljpeg code is in public domain and is therefore OK to be
included here.  I did minor modification to make the code compile under
modern Linux.
