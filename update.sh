#!/bin/bash

curl -s https://api.github.com/repos/i1470s/IVRY-Discord-Bot/releases/latest \
  | grep browser_download_url \
  | grep linux64 \
  | cut -d '"' -f 4 \
  | wget -qi -