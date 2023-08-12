#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#new
PATH_TO_CONFIG="$HOME/.config/qtile"
[ ! -f "$PATH_TO_CONFIG/palettes/decay/colors.json" ] && "$PATH_TO_CONFIG/color/colors.py"
for tool in picom eww dunst; do
	pkill $tool &
done
sleep 1

#new


#starting utility applications at boot time
lxsession &
run nm-applet &
run pamac-tray &
numlockx on &
blueman-applet &
#flameshot &
#picom --config $HOME/.config/picom/picom.conf &
picom --config "$PATH_TO_CONFIG/picom/picom-animations.conf" &
# picom --config ~/.config/picom/picom-animations.conf --experimental-backends --backend glx &
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#dunst &
	cat "$PATH_TO_CONFIG/dunst/dunstrc" | dunst -conf - &

#feh --randomize --bg-fill ~/Pictures/Wallpapers/* &

# eww -c "$PATH_TO_CONFIG/eww daemon" &

# eww -c "$PATH_TO_CONFIG/eww" open bar0 &

# feh --bg-fill /usr/share/wallpapers/garuda-wallpapers/qtile.jpg
#starting user applications at boot time
run volumeicon &
clipster -d &
#run discord &
#nitrogen --random --set-zoom-fill &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run telegram-desktop &
