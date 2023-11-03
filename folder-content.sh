#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
cd docs
FILES="*.md"
for f in $FILES
do
  echo "- [$f]($f)"
done
