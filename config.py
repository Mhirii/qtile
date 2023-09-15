import os
import subprocess

from core.keys import keys
from core.groups import groups
from core.mods import mod
from core.float import float_rules, floating_types
from core.screen import init_screens
from core.mouse import mouse
from libqtile import layout
import core.hooks
from core.layouts import init_layout_theme, init_layouts
from libqtile.config import Group, ScratchPad, DropDown

auto_fullscreen = True


focus_on_window_activation = "focus"  # or smart

wmname = "Qtile"

layout_theme = init_layout_theme()
layouts = init_layouts()
screens = init_screens()
mouse = mouse

main = None

follow_mouse_focus = True
bring_front_click = False
cursor_warp = True 
floating_layout = layout.Floating(
    float_rules(),
    fullscreen_border_width=0,
    border_width=0,
)
