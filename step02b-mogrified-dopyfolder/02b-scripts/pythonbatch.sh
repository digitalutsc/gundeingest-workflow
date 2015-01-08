#!/bin/bash
yourfolder=batch3
yourfolder2=batch06

for f in $yourfolder2/*
do 
python bookbatch2.py $f gundepynew/py$f

done


# for f in $yourfolder2/*
# do 
# python bookbatch2.py $f gundepynew/py$f

# done