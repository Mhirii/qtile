from core.utils import change_theme
from libqtile.lazy import lazy

mocha = {
    "bg": "#11111b",
    "bg1": "#1e1e2e",
    "bg2": "#45475a",
    "bg3": "#6c7086",
    "text": "#bac2de",
    "text1": "#cdd6f4",
    "1": "#b4befe",
    "2": "#f38ba8",
    "3": "#f9e2af",
    "4": "#74c7ec",
    "5": "#89dceb",
    "6": "#a6e3a1",
    "icon_path": "/home/mhiri/.config/qtile/assets/mocha/",
}
decay_dark = {
    "bg": "#101419",
    "bg1": "#181c21",
    "bg2": "#1c252c",
    "bg3": "#3c4a4c",
    "text": "#b6beca",
    "text1": "#b6beca",
    "1": "#94f7c5",
    "2": "#fc7b81",
    "3": "#ffeba6",
    "4": "#8cc1ff",
    "5": "#90daff",
    "6": "#e2a6ff",
    "icon_path": "/home/mhiri/.config/qtile/assets/mocha/",
}
nord = {
    "name": "nord",
    "bg": "#2A2F3A",
    "bg1": "#3B4252",
    "bg2": "#687591",
    "bg3": "#7f8ca9",
    "text": "#C8CED9",
    "text1": "#8E95A4",
    "1": "#D06F79",
    "2": "#a3be8c",
    "3": "#ebcb8b",
    "4": "#88c0d0",
    "5": "#b48ead",
    "6": "#8fbcbb",
    "icon_path": "/home/mhiri/.config/qtile/assets/nord/",
    "vscode": "Nord",
    "kitty": "Nord",
}
tokyonight = {
    "name": "tokyonight",
    "bg": "#16161e",
    "bg1": "#1a1b26",
    # "bg2": "#323749",
    "bg2": "#24283b",
    "bg3": "#414868",
    "text": "#a9b1d6",
    "text1": "#c0caf5",
    "1": "#9ece6a",
    "2": "#f7768e",
    "3": "#e0af68",
    "4": "#7aa2f7",
    "5": "#7dcfff",
    "6": "#bb9af7",
    "icon_path": "/home/mhiri/.config/qtile/assets/mocha/",
    "vscode": "Tokyo Night",
    "kitty": "Tokyo Night",
}
onedark = {
    "name": "onedark",
    "bg": "#21252b",
    "bg1": "#282c34",
    "bg2": "#313640",
    "bg3": "#5a5f6d",
    "text": "#abb2bf",
    "text1": "#bbc2cf",
    "1": "#e06c75",
    "2": "#98c379",
    "3": "#e5c07b",
    "4": "#61afef",
    "5": "#c678dd",
    "6": "#56b6c2",
    "icon_path": "/home/mhiri/.config/qtile/assets/mocha/",
    "vscode": "One Dark Pro Flat",
    "kitty": "One Dark",
}

def cycle_theme():
    global theme_index, theme, theme_name, accent, error, success, warning
    theme_index = (theme_index + 1) % len(themes)
    theme = themes[theme_index]
    theme_name = theme["name"]
    lazy.restart()


themes = [tokyonight, onedark]
theme_index = 0

theme = themes[theme_index]
theme_name = theme["name"]
accent = theme["4"]
error = theme["1"]
success = theme["2"]
warning = theme["3"]



change_theme(theme, accent, error)
