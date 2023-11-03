#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
FILES="./*.do*"
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  npx mammoth $f --output-format=markdown > $f.md
done
