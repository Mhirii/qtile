from libqtile.config import Group, ScratchPad, DropDown
from core import apps
from core.matches import (
    code_editors,
    browsers,
    discord,
    terminals,
    file_browsers,
    password_managers,
    git_managers,
    music_players,
    mail_clients,
)
from core.settings import workspaces

from libqtile.config import Key
from libqtile.lazy import lazy

from core.screen import num_screens, hostname
from core.keys import keys, mod, mod1, mod2

groups = [
    Group("a", label="A", init=True, spawn=apps.TERM_EMULATOR),
    Group("s", label="S", init=True),
    Group("d", label="D", init=True, spawn=apps.EDITOR),
    Group("f", label="F", init=True, spawn=apps.FILEMANAGER),
    Group("1", label="Ⅰ", init=True),
    Group("2", label="Ⅱ", init=True),
    Group("3", label="Ⅲ", init=True),
    Group("4", label="Ⅳ", init=True),
    Group("5", label="Ⅴ", init=True, matches=discord),
    Group("6", label="Ⅵ", init=True, matches=music_players),
    Group("u", label="U", init=True, matches=password_managers),
    Group("i", label="I", init=True, matches=git_managers),
    Group("o", label="O", init=True, matches=mail_clients),
    Group("p", label="P", init=True),
]

for index, i in enumerate(groups):
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(workspaces[index]['screen']),
                lazy.to_screen(workspaces[index]['screen']),
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
                lazy.group[i.name].toscreen(workspaces[index]['screen']),
            ),
        ]
    )
