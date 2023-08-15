from libqtile.config import Key
from libqtile.lazy import lazy
from core.settings import apps
from core.utils import change_theme
from assets import themes

mod = "mod4"
mod1 = "alt"
mod2 = "control"

keys = [
    Key(*key)
    for key in [
        #
        #
        # █████████
        # ███░░░░░███
        # ░███    ░███  ████████  ████████   █████
        # ░███████████ ░░███░░███░░███░░███ ███░░
        # ░███░░░░░███  ░███ ░███ ░███ ░███░░█████
        # ░███    ░███  ░███ ░███ ░███ ░███ ░░░░███
        # █████   █████ ░███████  ░███████  ██████
        # ░░░░░   ░░░░░  ░███░░░   ░███░░░  ░░░░░░
        #                ░███      ░███
        #                █████     █████
        #                ░░░░░     ░░░░░
        #
        #
        ([mod], "e", lazy.spawn(apps["files"])),
        ([mod], "t", lazy.spawn(apps["terminal"])),
        ([mod, "shift"], "t", lazy.spawn(apps["terminal_two"])),
        ([mod, "control"], "t", lazy.spawn(apps["terminal_three"])),
        ([mod], "c", lazy.spawn(apps["editor"])),
        ([mod], "b", lazy.spawn(apps["browser"])),
        ([mod], "m", lazy.spawn(apps["music_player"])),
        ([], "XF86Mail", lazy.spawn(apps["mail"])),
        ([mod2, "shift"], "Escape", lazy.spawn("lxtask")),
        # ([mod], "r", lazy.spawn("rofi -show drun")),
        ([mod], "r", lazy.spawn(apps["rofi"])),
        ([mod], "space", lazy.spawn(apps["dmenu"])),
        #
        #
        #              █████     ███  ████   ███   █████
        #             ░░███     ░░░  ░░███  ░░░   ░░███
        #  █████ ████ ███████   ████  ░███  ████  ███████   █████ ████
        # ░░███ ░███ ░░░███░   ░░███  ░███ ░░███ ░░░███░   ░░███ ░███
        #  ░███ ░███   ░███     ░███  ░███  ░███   ░███     ░███ ░███
        #  ░███ ░███   ░███ ███ ░███  ░███  ░███   ░███ ███ ░███ ░███
        #  ░░████████  ░░█████  █████ █████ █████  ░░█████  ░░███████
        #   ░░░░░░░░    ░░░░░  ░░░░░ ░░░░░ ░░░░░    ░░░░░    ░░░░░███
        #                                                    ███ ░███
        #                                                   ░░██████
        #                                                   ░░░░░░
        #
        ([mod], "v", lazy.spawn(apps["clipboard"])),
        ([mod], "prior", lazy.spawn(apps["colorpicker"])),
        # ([mod], "p", lazy.spawn(f"{ROFI_BIN}/powermenu.sh")),
        # ([mod], "w", change_theme(themes.theme, themes.accent, themes.error)),
        ([mod], "Escape", lazy.spawn("xkill")),
        ([mod, "control"], "m", lazy.spawn("pavucontrol")),
        ([], "Print", lazy.spawn(apps["screenshot"])),
        #
        #
        #  █████ ███ █████ █████████████
        # ░░███ ░███░░███ ░░███░░███░░███
        #  ░███ ░███ ░███  ░███ ░███ ░███
        #  ░░███████████   ░███ ░███ ░███
        #   ░░████░████    █████░███ █████
        #    ░░░░ ░░░░    ░░░░░ ░░░ ░░░░░
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        ([mod], "left", lazy.layout.left()),
        ([mod], "right", lazy.layout.right()),
        ([mod], "down", lazy.layout.down()),
        ([mod], "up", lazy.layout.up()),
        ([mod, "shift"], "h", lazy.layout.shuffle_left()),
        ([mod, "shift"], "l", lazy.layout.shuffle_right()),
        ([mod, "shift"], "j", lazy.layout.shuffle_down()),
        ([mod, "shift"], "k", lazy.layout.shuffle_up()),
        ([mod, "shift"], "left", lazy.layout.shuffle_left()),
        ([mod, "shift"], "right", lazy.layout.shuffle_right()),
        ([mod, "shift"], "down", lazy.layout.shuffle_down()),
        ([mod, "shift"], "up", lazy.layout.shuffle_up()),
        (
            [mod, "control"],
            "l",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        (
            [mod, "control"],
            "h",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        (
            [mod, "control"],
            "k",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        (
            [mod, "control"],
            "j",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        (
            [mod, "control"],
            "right",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        (
            [mod, "control"],
            "left",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        (
            [mod, "control"],
            "up",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        (
            [mod, "control"],
            "down",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        # qtile stuff
        ([mod], "Pause", lazy.spawn("betterlockscreen -l")),
        ([mod, "control"], "Pause", lazy.shutdown()),
        ([mod, "shift"], "Pause", lazy.spawn(apps["rofi_power"])),
        ([mod, "control"], "b", lazy.hide_show_bar()),
        ([mod, "control"], "r", lazy.restart()),
        # window management
        ([mod], "n", lazy.layout.normalize()),
        ([mod], "q", lazy.window.kill()),
        ([], "F11", lazy.window.toggle_fullscreen()),
        ([mod], "y", lazy.window.toggle_floating()),
        ([mod], "Tab", lazy.next_layout()),
        # fn keys
        ([], "XF86Tools", lazy.spawn("nwggrid -p -o 0.4")),
        ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
        ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%- ")),
        ([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
        ([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
        ([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
        ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
        ([], "XF86AudioNext", lazy.spawn("playerctl next")),
        ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
        ([], "XF86AudioStop", lazy.spawn("playerctl stop")),
        # Key(
        #     ["mod1", "control"],
        #     "o",
        #     lazy.spawn(home + "/.config/qtile/scripts/picom-toggle.sh"),
        # ),
        # Key([], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures/Screenshots")),
    ]
]
#
#
#    █████████                                             █████
#   ███░░░░░███                                           ░░███
#  ███     ░░░  ████████   ██████  █████ ████ ████████     ░███ █████  ██████  █████ ████  █████
# ░███         ░░███░░███ ███░░███░░███ ░███ ░░███░░███    ░███░░███  ███░░███░░███ ░███  ███░░
# ░███    █████ ░███ ░░░ ░███ ░███ ░███ ░███  ░███ ░███    ░██████░  ░███████  ░███ ░███ ░░█████
# ░░███  ░░███  ░███     ░███ ░███ ░███ ░███  ░███ ░███    ░███░░███ ░███░░░   ░███ ░███  ░░░░███
#  ░░█████████  █████    ░░██████  ░░████████ ░███████     ████ █████░░██████  ░░███████  ██████
#   ░░░░░░░░░  ░░░░░      ░░░░░░    ░░░░░░░░  ░███░░░     ░░░░ ░░░░░  ░░░░░░    ░░░░░███ ░░░░░░
#                                             ░███                              ███ ░███
#                                             █████                            ░░██████
#                                            ░░░░░                              ░░░░░░


"""
if num_screens[hostname] == 2:
    k = [
        "a",
        "s",
        "d",
        "f",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "u",
        "i",
        "o",
        "p",
    ]
    g = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
else:
    k = ["1", "2", "3", "4", "equal"]
    g = [0, 0, 0, 0, 0]

for index, i in enumerate(groups):
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(g[index]),
                lazy.to_screen(g[index]),
                desc="Switch to group {}".format(i.name),
            ),
            Key([mod, mod2], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
            Key(
                ["mod1"],
                "Tab",
                lazy.group.next_window(),
            ),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            Key([mod, "mod1"], i.name, lazy.window.togroup(i.name)),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                lazy.group[i.name].toscreen(g[index]),
            ),
        ]
    )
"""
