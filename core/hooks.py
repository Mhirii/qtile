from libqtile import hook
import os
import subprocess
from pathlib import Path
from core.float import floating_types
from core.state import State

state = State()
HOME = f"{Path.home()}/"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
            window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


@hook.subscribe.layout_change
@hook.subscribe.client_new
@hook.subscribe.changegroup
@hook.subscribe.focus_change
async def _(*args):
    state.update_state()
