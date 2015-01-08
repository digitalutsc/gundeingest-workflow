#!/bin/bash

# for dir in ../DARK/*; do (cd "$dir" && pwd && mogrify -auto-level *.tif); done
# for dir in ../moderate/*; do (cd "$dir" && pwd && mogrify -auto-level *.tif); done
for dir in ../batch05/*; do (cd "$dir" && pwd && mogrify -auto-level *.tif); done
# for dir in somewhatdark/*; do (cd "$dir" && pwd && mogrify -auto-level *.tif); done