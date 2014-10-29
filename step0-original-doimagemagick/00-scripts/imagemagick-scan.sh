#!/bin/bash

for dir in /Users/dsuuser/Desktop/kim/gunde/STEP1-imagemagick/*; do (cd "$dir" && pwd && identify *.tif); done