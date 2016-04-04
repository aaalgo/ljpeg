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

	The loaded is a matrix of type uint16.


The Stanford ljpeg code is in public domain and is therefore OK to be
included here.  I did minor modification to make the code compile under
modern Linux.
