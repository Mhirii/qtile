from libqtile import widget, qtile

from assets.themes import theme, icon, accent
from core.apps import TERM_EMULATOR
from dbus_next import *
from libqtile.command import lazy


#    
def seperator_pipe(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=25,
        padding=0,
        background=bg,
        foreground=fg,
        font="SauceCodeMono Nerd Font",
    )


def seperator_pipe_reverse(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=25,
        padding=0,
        background=bg,
        foreground=fg,
        font="SauceCodeMono Nerd Font",
    )


def slash(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=25,
        padding=0,
        background=bg,
        foreground=fg,
        font="SauceCodeMono Nerd Font",
    )


def slash_reverse(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=25,
        padding=0,
        background=bg,
        foreground=fg,
        font="SauceCodeMono Nerd Font",
    )


pipes_bar = [
    widget.Spacer(
        length=8,
        background=theme["bg"],
    ),
    widget.TextBox(
        text=" ",
        fontsize=18,
        padding=4,
        background=theme["bg"],
        foreground=accent,
        font="SauceCodeMono Nerd Font",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("jgmenu_run")},
    ),
    seperator_pipe(theme["bg1"], theme["bg"]),
    widget.GroupBox(
        font="JetBrainsMono Nerd Font Bold",
        fontsize=16,
        borderwidth=2,
        highlight_method="block",
        background=theme["bg1"],
        inactive=theme["bg2"],
        active=theme["bg3"],
        block_highlight_text_color=accent,
        highlight_color="#4B427E",
        foreground="#4B427E",
        this_current_screen_border=theme["bg1"],
        this_screen_border=theme["bg1"],
        other_current_screen_border=theme["bg1"],
        other_screen_border=theme["bg1"],
        urgent_alert_method="block",
        urgent_border="#af5555",
        rounded=True,
        hide_unused=True,
        disable_drag=True,
    ),
    widget.Spacer(
        length=8,
        background=theme["bg1"],
    ),
    seperator_pipe(theme["bg"], theme["bg1"]),
    widget.WidgetBox(
        background=theme["bg"],
        close_button_location="left",
        font="JetbrainsMono Nerd Font",
        fontshadow=None,
        fontsize=14,
        foreground=theme["1"],
        mouse_callbacks={},
        #    
        text_closed="  󰙀  ",
        text_open="  󰙀 ",
        widgets=[
            widget.CurrentLayout(
                background=theme["bg"],
                foreground=theme["1"],
                fmt="{}",
                font="JetBrainsMono Nerd Font Bold",
                fontsize=14,
            ),
            widget.Spacer(
                length=16,
                background=theme["bg"],
            ),
            slash(theme["bg"], theme["bg1"]),
            widget.Wallpaper(
                background=theme["bg"],
                foreground=theme["1"],
                font="JetBrainsMono Nerd Font Bold",
                fontsize=14,
                fmt=" 󰲍  {}",
                directory="~/Pictures/Wallpapers/",
                max_chars=40,
            ),
        ],
    ),
    seperator_pipe(theme["bg1"], theme["bg"]),
    widget.Spacer(
        background=theme["bg1"],
    ),
    widget.Spacer(
        background=theme["bg1"],
    ),
    seperator_pipe_reverse(theme["bg1"], theme["bg"]),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
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
    widget.CPU(
        background=theme["bg1"],
        format="  {load_percent}%",
        foreground=theme["5"],
        font="JetBrainsMono Nerd Font Bold",
        fontsize=14,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    ),
    widget.Spacer(
        length=16,
        background=theme["bg1"],
    ),
    widget.Memory(
        background=theme["bg1"],
        # format=" {MemPercent: .0f}{mm}",
        format=" {MemPercent}%",
        foreground=theme["5"],
        font="JetBrainsMono Nerd Font Bold",
        fontsize=14,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    ),
    widget.Spacer(
        length=16,
        background=theme["bg1"],
    ),
    widget.Volume(
        font="JetBrainsMono Nerd Font Bold",
        emoji=True,
        theme_path=icon["volume"],
        fontsize=14,
        background=theme["bg1"],
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    widget.Spacer(
        length=-10,
        background=theme["bg1"],
    ),
    widget.Volume(
        font="JetBrainsMono Nerd Font Bold",
        background=theme["bg1"],
        foreground=theme["5"],
        fontsize=14,
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    widget.Spacer(
        length=8,
        background=theme["bg1"],
    ),
    seperator_pipe_reverse(theme["bg1"], theme["bg"]),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
    widget.Clock(
        format="%A %d ",
        background=theme["bg"],
        foreground=accent,
        font="JetBrainsMono Nerd Font Ultra-Bold",
        fontsize=16,
    ),
    widget.Clock(
        format="%I:%M",
        background=theme["bg"],
        foreground=accent,
        font="JetBrainsMono Nerd Font Ultra-Bold",
        fontsize=16,
    ),
    widget.Spacer(
        length=8,
        background=theme["bg"],
    ),
]
pipes_bar_minimal = [
    widget.Spacer(
        length=8,
        background=theme["bg"],
    ),
    widget.TextBox(
        text=" ",
        fontsize=18,
        padding=4,
        background=theme["bg"],
        foreground=accent,
        font="SauceCodeMono Nerd Font",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("jgmenu_run")},
    ),
    seperator_pipe(theme["bg1"], theme["bg"]),
    widget.GroupBox(
        font="JetBrainsMono Nerd Font Bold",
        fontsize=16,
        borderwidth=2,
        highlight_method="block",
        background=theme["bg1"],
        inactive=theme["bg2"],
        active=theme["bg3"],
        block_highlight_text_color=accent,
        highlight_color="#4B427E",
        foreground="#4B427E",
        this_current_screen_border=theme["bg1"],
        this_screen_border=theme["bg1"],
        other_current_screen_border=theme["bg1"],
        other_screen_border=theme["bg1"],
        urgent_alert_method="block",
        urgent_border="#af5555",
        rounded=True,
        hide_unused=True,
        disable_drag=True,
    ),
    widget.Spacer(
        length=8,
        background=theme["bg1"],
    ),
    seperator_pipe(theme["bg"], theme["bg1"]),
    widget.WidgetBox(
        background=theme["bg"],
        close_button_location="left",
        font="JetbrainsMono Nerd Font",
        fontshadow=None,
        fontsize=14,
        foreground=theme["1"],
        mouse_callbacks={},
        #    
        text_closed="  󰙀  ",
        text_open="  󰙀 ",
        widgets=[
            widget.CurrentLayout(
                background=theme["bg"],
                foreground=theme["1"],
                fmt="{}",
                font="JetBrainsMono Nerd Font Bold",
                fontsize=14,
            ),
            widget.Spacer(
                length=16,
                background=theme["bg"],
            ),
            slash(theme["bg"], theme["bg1"]),
            widget.Wallpaper(
                background=theme["bg"],
                foreground=theme["1"],
                font="JetBrainsMono Nerd Font Bold",
                fontsize=14,
                fmt=" 󰲍  {}",
                directory="~/Pictures/Wallpapers/",
                max_chars=40,
            ),
        ],
    ),
    seperator_pipe(theme["bg1"], theme["bg"]),
    widget.Spacer(
        background=theme["bg1"],
    ),
    widget.Spacer(
        background=theme["bg1"],
    ),
    seperator_pipe_reverse(theme["bg1"], theme["bg1"]),
    widget.CPU(
        background=theme["bg1"],
        format="  {load_percent}%",
        foreground=theme["5"],
        font="JetBrainsMono Nerd Font Bold",
        fontsize=14,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    ),
    widget.Spacer(
        length=16,
        background=theme["bg1"],
    ),
    widget.Memory(
        background=theme["bg1"],
        # format=" {MemPercent: .0f}{mm}",
        format=" {MemPercent}%",
        foreground=theme["5"],
        font="JetBrainsMono Nerd Font Bold",
        fontsize=14,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    ),
    widget.Spacer(
        length=16,
        background=theme["bg1"],
    ),
    widget.Volume(
        font="JetBrainsMono Nerd Font Bold",
        emoji=True,
        theme_path=icon["volume"],
        fontsize=14,
        background=theme["bg1"],
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    widget.Spacer(
        length=-10,
        background=theme["bg1"],
    ),
    widget.Volume(
        font="JetBrainsMono Nerd Font Bold",
        background=theme["bg1"],
        foreground=theme["5"],
        fontsize=14,
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
    ),
    widget.Spacer(
        length=8,
        background=theme["bg1"],
    ),
    seperator_pipe_reverse(theme["bg1"], theme["bg"]),
    widget.TextBox(
        text=" ",
        background=theme["bg"],
    ),
    widget.Clock(
        format="%A %d ",
        background=theme["bg"],
        foreground=accent,
        font="JetBrainsMono Nerd Font Ultra-Bold",
        fontsize=16,
    ),
    widget.Clock(
        format="%I:%M",
        background=theme["bg"],
        foreground=accent,
        font="JetBrainsMono Nerd Font Ultra-Bold",
        fontsize=16,
    ),
    widget.Spacer(
        length=8,
        background=theme["bg"],
    ),
]


def init_widgets_list():
    widgets_list = pipes_bar
    return widgets_list


def init_widgets_list2():
    widgets_list2 = pipes_bar_minimal
    return widgets_list2
