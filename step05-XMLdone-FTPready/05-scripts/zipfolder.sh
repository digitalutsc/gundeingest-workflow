#!/bin/bash
for i in */; do zip -r "${i%/}.zip" "$i"; done

# zip not individual books but a folder of books.  zip one book you don't zip the enclosing folder you just zip the contents