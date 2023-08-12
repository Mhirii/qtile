from libqtile.config import Match

browsers = [
    Match(wm_class="firefox"),
    Match(wm_class="qutebrowser"),
    Match(wm_class="Brave-browser"),
    Match(wm_class="firedragon"),
]
terminals = [
    Match(wm_class="kitty"),
]
code_editors = [
    Match(wm_class="jetbrains-pycharm"),
    Match(wm_class="jetbrains-webstorm"),
    Match(wm_class="code-oss"),
]
file_browsers = [
    Match(wm_class="Thunar"),
]
music_players = [
    Match(wm_class="Spotify"),
    Match(title="spotify-tui"),
    Match(title="cava")
]
mail_clients=[
    Match(wm_class="thunderbirdbeta"),
    Match(wm_class="betterbird"),
    Match(wm_class="protonmail-nativefier-2572fe"),
]
git_managers=[
    Match(wm_class="GitKraken"),
    Match(wm_class="Gittyup"),
]
password_managers=[
    Match(wm_class="Bitwarden"),
]
discord=[Match(wm_class="discord")]
