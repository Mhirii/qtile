from dbus_next import *
from libqtile import qtile, widget
from libqtile.command import lazy

import assets.themes
from assets.themes import accent, cycle_theme, theme, theme_name
from core import settings
from core.widgets import *


def test_function():
    lazy.restart()

pipes_bar = [
    spacer(theme["bg"], 8),
    archlinux(),
    seperator_pipe(theme["bg1"], theme["bg"]),
    widget.GroupBox(
        font=settings.font_bold,
        fontsize=settings.fontsize,
        borderwidth=2,
        padding=2,
        highlight_method="block",
        background=theme["bg1"],
        inactive=theme["bg2"],
        active=theme["bg3"],
        block_highlight_text_color=accent,
        highlight_color="#4B427E",
        foreground="#4B427E",
        this_current_screen_border=theme["bg1"],
        this_screen_border=theme["bg1"],
        other_current_screen_border=theme["bg2"],
        other_screen_border=theme["bg1"],
        urgent_alert_method="text",
        # urgent_border="#181c21",
        urgent_text="#af5555",
        rounded=True,
        # hide_unused=True,
        disable_drag=True,
    ),
    spacer(theme["bg1"], 8),
    seperator_pipe(theme["bg"], theme["bg1"]),
    widget.WidgetBox(
        background=theme["bg"],
        close_button_location="left",
        font=settings.font_bold,
        fontshadow=None,
        fontsize=settings.fontsize,
        foreground=accent,
        mouse_callbacks={},
        #    
        text_closed="    ",
        text_open="   ",
        widgets=[
            slash(theme["bg"], theme["bg1"]),
            widget.Spacer(
                length=8,
                background=theme["bg"],
            ),
            widget.CurrentLayout(
                background=theme["bg"],
                foreground=accent,
                fmt="󰙀 {}",
                font=settings.font_bold,
                fontsize=settings.fontsize,
            ),
            widget.Spacer(
                length=8,
                background=theme["bg"],
            ),
            slash(theme["bg"], theme["bg1"]),
            widget.Wallpaper(
                background=theme["bg"],
                foreground=accent,
                font=settings.font_bold,
                fontsize=settings.fontsize,
                fmt=" 󰲍  {}",
                directory=f"~/.config/qtile/wallpapers/{theme['name']}",
                max_chars=40,
            ),
            widget.Spacer(
                length=8,
                background=theme["bg"],
            ),
            slash(theme["bg"], theme["bg1"]),
            widget.TextBox(
                text=f"  {theme_name}",
                fontsize=settings.fontsize,
                # padding=4,
                background=theme["bg"],
                foreground=accent,
                font=settings.font_bold,
                # mouse_callbacks={"Button1": cycle_theme()},
                mouse_callbacks={"Button1": test_function()},
            )
        ],
    ),
    seperator_pipe(theme["bg1"], theme["bg"]),
    regular_spacer(theme["bg1"]),
    seperator_pipe_reverse(theme["bg1"], theme["bg"]),
    widget.TextBox(text=" ", background=theme["bg"]),
    widget.Systray(
        padding=4,
        background=theme["bg"],
        fontsize=2,
        icon_size=16,
    ),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
    seperator_pipe_reverse(theme["bg"], theme["bg1"]),
    spacer(theme["bg1"], 8),
    cpu_widget(),
    slash_reverse(theme["bg1"], theme["bg"]),
    memory_widget(),
    slash_reverse(theme["bg1"], theme["bg"]),
    widget.NvidiaSensors( font=settings.font_bold, background=theme["bg1"], foreground=accent, foreground_alert=theme["2"], fontsize=settings.fontsize, ),
    slash_reverse(theme["bg1"], theme["bg"]),
    widget.Volume(
        font=settings.font_bold,
        background=theme["bg1"],
        foreground=accent,
        fontsize=settings.fontsize,
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    spacer(theme["bg1"], 8),
    seperator_pipe_reverse(theme["bg1"], theme["bg"]),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
    date(),
    time(),
    spacer(theme["bg"], 8),
]


pipes_bar_minimal = [
    spacer(theme["bg"], 8),
    archlinux(),
    seperator_pipe(theme["bg1"], theme["bg"]),
    widget.GroupBox(
        font=settings.font_bold,
        fontsize=settings.fontsize,
        borderwidth=2,
        # padding=2,
        highlight_method="block",
        background=theme["bg1"],
        inactive=theme["bg2"],
        active=theme["bg3"],
        block_highlight_text_color=accent,
        highlight_color="#4B427E",
        foreground="#4B427E",
        this_current_screen_border=theme["bg1"],
        this_screen_border=theme["bg1"],
        other_current_screen_border=theme["bg2"],
        other_screen_border=theme["bg1"],
        urgent_alert_method="text",
        # urgent_border="#181c21",
        urgent_text="#af5555",
        rounded=True,
        hide_unused=True,
        disable_drag=True,
    ),
    spacer(theme["bg1"], 8),
    seperator_pipe(theme["bg"], theme["bg1"]),
    widget.WidgetBox(
        background=theme["bg"],
        close_button_location="left",
        font=settings.font_bold,
        fontshadow=None,
        fontsize=settings.fontsize,
        foreground=accent,
        mouse_callbacks={},
        #    
        text_closed="  󰙀  ",
        text_open="  󰙀 ",
        widgets=[
            widget.CurrentLayout(
                background=theme["bg"],
                foreground=accent,
                fmt="{}",
                font=settings.font_bold,
                fontsize=settings.fontsize,
            ),
        ],
    ),
    seperator_pipe(theme["bg1"], theme["bg"]),
    regular_spacer(theme["bg1"]),
    regular_spacer(theme["bg1"]),
    seperator_pipe_reverse(theme["bg1"], theme["bg1"]),
    spacer(theme["bg1"], 8),
    cpu_widget(),
    slash_reverse(theme["bg1"], theme["bg"]),
    memory_widget(),
    slash_reverse(theme["bg1"], theme["bg"]),
    widget.Volume(
        font=settings.font_bold,
        background=theme["bg1"],
        foreground=accent,
        fontsize=settings.fontsize,
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    spacer(theme["bg1"], 8),
    seperator_pipe_reverse(theme["bg1"], theme["bg"]),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
    date(),
    time(),
    spacer(theme["bg"], 8),
]

def init_widgets_list():
    widgets_list = pipes_bar
    return widgets_list


def init_widgets_list2():
    widgets_list2 = pipes_bar_minimal
    return widgets_list2
