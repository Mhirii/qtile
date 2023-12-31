workspaces = [
    {"name": "a", "label": "A", "key": "a", "screen": 0},
    {"name": "s", "label": "S", "key": "s", "screen": 0},
    {"name": "d", "label": "D", "key": "d", "screen": 0},
    {"name": "f", "label": "F", "key": "f", "screen": 0},
    {"name": "1", "label": "Ⅰ", "key": "1", "screen": 1},
    {"name": "2", "label": "Ⅱ", "key": "2", "screen": 1},
    {"name": "3", "label": "Ⅲ", "key": "3", "screen": 1},
    {"name": "4", "label": "Ⅳ", "key": "4", "screen": 1},
    {"name": "5", "label": "Ⅴ", "key": "5", "screen": 1},
    {"name": "6", "label": "Ⅵ", "key": "6", "screen": 1},
    {"name": "u", "label": "U", "key": "u", "screen": 0},
    {"name": "i", "label": "I", "key": "i", "screen": 0},
    {"name": "o", "label": "O", "key": "o", "screen": 0},
    {"name": "p", "label": "P", "key": "p", "screen": 0},
]

apps = {
    "browser": "firefox",
    "terminal": "kitty",
    "terminal_two": "wezterm",
    "terminal_three": "alacritty",
    # "editor": "rofi-code",
    "editor": "code --password-store='gnome'",
    "passwords": "bitwarden-desktop",
    "gitmanager": "gitkraken",
    "mail": "betterbird",
    "files": "thunar",
    "music_player": "spotify",
    "wallpaper": "sh -c ~/Scripts/wallpaper.sh",
    "clipboard": "roficlip",
    "screenshot": "flameshot full -p /home/mhiri/Pictures/Screenshots",
    "colorpicker": "sh -c ~/Scripts/colorpicker.sh",
    "rofi": "sh -c ~/.config/qtile/scripts/rofi.sh",
    "rofi_power": "sh -c ~/.config/qtile/scripts/power",
    "dmenu": "dmenu_run -i -nb '#16161e' -nf '#7aa2f7' -sb '#7aa2f7' -sf '#16161e' -fn 'SpaceMono Nerd Font:bold:pixelsize:24'",
    "hotel": "trivago",
}

font = "SpaceMono Nerd Font"
font_bold = "SpaceMono Nerd Font bold"
fontsize = 16
fontsize_med = 18
fontsize_big = 20

#                         󰇰    󰃮  󰆍  󰊫  󰓅  󰓇  󰡳 󰡵 󰡴  󰾆 󰾅 󰨞
# 󰫃 󰫄 󰫅 󰫆 󰫇 � 󰭟 󰭦 󰮯 󰯉 󰲍 󰵮 󰸘 󰸗 󱉫 󱉬 󱉨 󱎂 󱓝 󰏃 󰫢 󰒘   󰐣
# 󰸶 󰸸 󰸷 󰸴 󰸵 󰸳 󱂈 󱂉 󱂊 󱂋 󱂌 󱂍 󱂎 󱂏 󱂐 󱂑 󱉽 󱉼
# greek αβγδεζηθικ ΑΒΓΔΕΖΗΘΙΚ
# roman ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪ