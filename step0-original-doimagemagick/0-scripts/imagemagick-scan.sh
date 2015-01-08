#!/bin/bash

for dir in /Users/dsuuser/Desktop/kim/gunde/workflow/step0-original-doimagemagick/identify/*; do (cd "$dir" && pwd && identify *.tif); done