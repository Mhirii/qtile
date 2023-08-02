from libqtile.config import Screen
from libqtile import bar, widget
import platform
from core.bars import init_widgets_list
from core.bars import init_widgets_list2

# Number of screens on machines I use regularly. I wish there was a good way to
# query this from qtile...
"""
"""
hostname = platform.node()
num_screens = {
    "laptop": 1,
    "Desktop-G": 2,
    "hopstrocity": 1,
    "xephyr": 1,
}


def init_screens():
    if num_screens[hostname] == 2:
        return [
            Screen(
                top=bar.Bar(
                    widgets=init_widgets_list2(),
                    size=35,
                    opacity=1,
                    # background="000000",
                    border_color="#282738",
                    border_width=[0, 0, 0, 0],
                    margin=[0, 0, 0, 0],
                ),
            ),
            Screen(
                top=bar.Bar(
                    widgets=init_widgets_list(),
                    size=35,
                    opacity=1,
                    # background="000000",
                    border_color="#282738",
                    border_width=[0, 0, 0, 0],
                    margin=[0, 0, 0, 0],
                ),
            ),
        ]
    else:
        # 1 screen
        return [
            Screen(
                top=bar.Bar(
                    widgets=init_widgets_list(),
                    size=35,
                    opacity=1,
                    # background="000000",
                    border_color="#282738",
                    border_width=[0, 0, 0, 0],
                    margin=[0, 0, 0, 0],
                ),
            ),
        ]


"""
def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(),
                size=35,
                opacity=1,
                # background="000000",
                border_color="#282738",
                border_width=[0, 0, 0, 0],
                margin=[0, 0, 0, 0],
            )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list2(),
                size=35,
                opacity=1,
                # background="000000",
                border_color="#282738",
                border_width=[0, 0, 0, 0],
                margin=[0, 0, 0, 0],
            )
        ),
    ]
"""
