#!/bin/bash

for dir in reallydark/*/*; do (cd "$dir" && pwd && mogrify -auto-level *.tif); done