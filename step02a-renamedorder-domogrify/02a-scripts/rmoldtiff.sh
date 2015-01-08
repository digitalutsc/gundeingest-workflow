#!/bin/bash
# find . -name "*.tif~" -exec rm -rf {} \;
# it will look in every folder that it's in, you needed to do this with the old version of imagemagick mogrify.  new mogrify imagemagick version (since ImageMagick-x86_64-apple-darwin14.0.0.tar.gz) does not create the .tif~ file
find . -name "*.tif~" -exec mv {} /Users/dsuuser/Desktop/kim/gunde/workflow/step02a-renamedorder-domogrify/oldTIFF \;

