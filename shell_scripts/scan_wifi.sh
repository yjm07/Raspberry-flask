#! /bin/bash

# IFS_backup="$IFS"
# IFS='$\n'
list=$(sudo iwlist wlan0 scan | fgrep -B 3 ESSID | cut -d ':' -f 2 | cut -d '=' -f 2 | cut -d '/' -f 1 | awk '{print$1}')
# arr=()
# for word in $list; do
#     if $word=='--'; then
#         arr+=($word)
# done
# IFS=$IFS_backup
echo $list