import json
from pathlib import Path

try:
    with (Path.home() / ".config/qtile/palettes/decay/colors.json").open("r") as f:
        color = json.load(f)
except FileNotFoundError:
    color = {"name": "mauve", "hex": "#DDB6F2"}

BROWSER = "firefox"
TERM_EMULATOR = "wezterm"
TERM_EMULATOR_TWO = "kitty"
TERM_EMULATOR_THREE = "alacritty"
EDITOR = "code"
PASSWORDMANAGER = "bitwarden-desktop"
GITMANAGER = "gitkraken"
MAIL = "betterbird"
FILEMANAGER = "thunar"
MUSIC_PLAYER = "spotify"
WALLPAPER = "sh -c ~/Scripts/wallpaper.sh"
CLIPBOARD = "roficlip"
SCREENSHOT = "flameshot full -p /home/mhiri/Pictures/Screenshots"
COLORPICKER = "sh -c ~/Scripts/colorpicker.sh"
ROFI = "sh -c ~/.config/qtile/scripts/rofi.sh"
ROFIPOWER = "sh -c ~/.config/qtile/scripts/rofi/power"
DMENU = "dmenu_run -i -nb '#1e1e2e' -nf '#74c7ec' -sb '#cba6f7' -sf '#1e1e2e' -fn 'NotoMonoRegular:bold:pixelsize=24'"
HOTEL = "trivago"
