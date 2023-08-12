from libqtile import layout
from assets.themes import theme, accent


def init_layout_theme():
    return {
        "margin": 4,
        "border_width": 2,
        "border_focus": theme["5"],
        "border_normal": theme["bg1"],
    }


def init_layouts():
    layouts = [
        layout.Tile(
            add_after_last=True,
            margin=8,
            border_focus=accent,
            border_normal=theme["bg1"],
            border_width=2,
        ),
        layout.Zoomy(
            columnwidth=150,
            margin=4,
            property_big="1.0",
            property_name="ZOOM",
            property_small="0.1",
        ),
        layout.Columns(
            margin=[16, 16, 16, 16],
            border_focus=accent,
            border_normal=theme["bg1"],
            border_width=2,
            border_on_single=True,
            insert_position=1,
            margin_on_single=[32, 32, 32, 32],
            num_columns=2,
            wrap_focus_columns=True,
            wrap_focus_rows=True,
            wrap_focus_stacks=True,
        ),
        # layout.MonadTall(border_focus=theme["1"], border_normal=theme["bg"], margin=4, border_width=2),
    ]
    return layouts


floating_types = ["notification", "toolbar", "splash", "dialog"]
