#!/bin/bash

# Automatically change the lockscreen wallpaper
# replace with the path to your pics directory
filename_array=( $( ls ~/.config/qtile/wallpapers/ | sort --random-sort ) ) 
while (( 1==1 )); do
	for file in "${filename_array[@]}";do
		betterlockscreen -u ~/.config/qtile/wallpapers/"$file"
		sleep 0.5m
	done
done