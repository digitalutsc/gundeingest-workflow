#Gunda Gunde Manuscript workflow to ingest into islandora

##Introduction

Scripts and instructions in each folder are provided to reorganize the original optimized images into the book structure suitable for ingest into Islandora


##Instructions
The idea is to move each 'book' into each successive folder to perform the script

step0-original-doimagemagick - RUN batch script to scan all .TIFs and identify corrupt images

step01-imagemagicked-dorenameorder - THIS REQUIRES MANUAL ATTENTION. rename the appropriate files so that the images will be in the correct sequence for ingest

step02-renameordered-dopyfolder - RUN batch script which will batch run bookbatch.py

step03-pyfolder-dorenamefolder - For now, you should use a program like namechanger to rename all of the images to OBJ.tif and the folders to a numeric sequence: 01, 02, 03...  

step04-renamedfolder-domanualXML - put the xml as MODS.xml in the book level.  see additional note.

step05-XMLdone-FTPready - ready for ingest.  zip if you plan on using the zip importer.
