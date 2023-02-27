.. image:: https://readthedocs.org/projects/pyscaffold-demo/badge/?version=latest
    :alt: ReadTheDocs
    :target: https://pyscaffold-demo.readthedocs.io/

.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/demo-project.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/demo-project
    .. image:: https://readthedocs.org/projects/demo-project/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://demo-project.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/demo-project/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/demo-project
    .. image:: https://img.shields.io/pypi/v/demo-project.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/demo-project/
    .. image:: https://img.shields.io/conda/vn/conda-forge/demo-project.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/demo-project
    .. image:: https://pepy.tech/badge/demo-project/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/demo-project
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/demo-project

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

============
ljpeg
============
     Read and transform LJPEG images into modern formats.

Installation
============
Warning: You must have installed the flex parser on your operating system::

    pip install ljpeg

By default, we offer you a binary called jpeg_static. However, you can produce your jpeg binary::

    cd jpegdir && make

Getting started
=================
Download a set of mammograms with::

     wget -r -q ftp://figment.csee.usf.edu:21/pub/DDSM/cases/normals/normal_08/case4606/

Transform a lot of mammograms parallely::

     find . -type f -name '*.LJPEG' | parallel -j+0 "ljpeg {} $(pwd)/{/.}.tiff --verify"

Convert to TIFF (requires the .ics file in the same directory as LJPEG)::

     ljpeg $(pwd)/C_0029_1.LEFT_CC.LJPEG $(pwd)/output.tiff


Convert to TIFF and verify that no information has been lost::

      ljpeg $(pwd)/C_0029_1.LEFT_CC.LJPEG $(pwd)/output.tiff --verify

Convert to jpeg for visualization with down-sizing scale=0.3 (16-bit TIFF is not good for direct visualization)::

      ljpeg $(pwd)/C_0029_1.LEFT_CC.LJPEG $(pwd)/output.jpg --visual --scale 0.3

Note that output file can be any format that's supported by OpenCV (which includes all common types). Most file formats only support 8-bit images, so directly saving into such file formats will cause problems. Add "--visual" to normalize color into 8-bit before saving to such file formats.

The Stanford ljpeg code is in public domain and is therefore OK to be included here. I did minor modification to make the code compile under modern Linux.


Making Changes & Contributing
=============================

This project uses `pre-commit`_, please make sure to install it before making any
changes::

    pip install pre-commit
    cd demo-project
    pre-commit install

It is a good idea to update the hooks to the latest version::

    pre-commit autoupdate

Don't forget to tell your contributors to also install and use pre-commit.

.. _pre-commit: https://pre-commit.com/

Note
====

This project has been set up using PyScaffold 4.2.2.post1.dev3+g01e6e81. For details and usage
information on PyScaffold see https://pyscaffold.org/.
