#!/bin/bash

set -eu

wget -q https://github.com/tiann/KernelSU/raw/main/website/docs/repos.json

echo "# Repo Check Status"
echo
echo "Updated on $(date '+%Y-%m-%dT%H:%M:%S')"
echo
echo "| repo url | repo status |"
echo "| -------- | -------- | "

python3 bin/geturl.py
python3 bin/checkurl.py | grep 301
python3 bin/checkurl.py | grep 404
