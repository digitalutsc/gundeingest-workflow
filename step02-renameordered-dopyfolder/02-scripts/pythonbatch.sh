#!/bin/bash
yourfolder=batch1

for f in $yourfolder/*
do 
python bookbatch2.py $f gundepynew/py-$f

done