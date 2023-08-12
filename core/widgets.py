from libqtile import widget, qtile
from assets.themes import theme, accent
from core.apps import TERM_EMULATOR
from core import settings

def seperator_pipe(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=25,
        padding=0,
        background=bg,
        foreground=fg,
        font=settings.font_bold,
    )


def seperator_pipe_reverse(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=25,
        padding=0,
        background=bg,
        foreground=fg,
        font=settings.font_bold,
    )


def slash(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=25,
        padding=0,
        background=bg,
        foreground=fg,
        font=settings.font_bold,
    )


def slash_reverse(bg, fg):
    return widget.TextBox(
        text="",
        fontsize=25,
        padding=0,
        background=bg,
        foreground=fg,
        font=settings.font_bold,
    )


def archlinux():
    return widget.TextBox(
        text=" ",
        fontsize=settings.fontsize_big,
        padding=4,
        background=theme["bg"],
        foreground=accent,
        font=settings.font_bold,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("jgmenu_run")},
    )


def regular_spacer(bg):
    return widget.Spacer(
        background=bg,
    )


def spacer(bg, space):
    return widget.Spacer(
        length=space,
        background=bg,

    )


def cpu_widget():
    return widget.CPU(
        background=theme["bg1"],
        format="{load_percent}%",
        foreground=accent,
        font=settings.font_bold,
        fontsize=settings.fontsize,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    )


def memory_widget():
    return widget.Memory(
        background=theme["bg1"],
        format="{MemPercent}%",
        foreground=accent,
        font=settings.font_bold,
        fontsize=settings.fontsize,
        update_interval=5,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(TERM_EMULATOR + " -e htop")
        },
    )


def date():
    return widget.Clock(
        format="%A %d ",
        background=theme["bg"],
        foreground=accent,
        font=settings.font_bold,
        fontsize=settings.fontsize,
    )


def time():
    return widget.Clock(
        format="%I:%M",
        background=theme["bg"],
        foreground=accent,
        font=settings.font_bold,
        fontsize=settings.fontsize,
    )
