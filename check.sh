#!/bin/bash

set -eu

echo "# KernelSU repo status"
echo
echo "Updated on $(date '+%Y-%m-%dT%H:%M:%S')"
echo
echo "| repo url | repo status |"
echo "| -------- | -------- | "

python3 bin/geturl.py
python3 bin/checkurl.py | grep 301
python3 bin/checkurl.py | grep 404
