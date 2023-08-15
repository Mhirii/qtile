import os
import subprocess


def write_rofi_theme(desired_theme, accent, error):
    rofi_theme_path = os.path.expanduser(f"~/.config/qtile/rofi/themes/{desired_theme['name']}.rasi")
    rofi_theme = f"""
    *{{
    background: {desired_theme["bg1"]}e6;
    background-alt: {desired_theme["bg2"]}b4;
    text: {desired_theme["text"]}ff;
    text-dark: {desired_theme["bg1"]}ff;
    selected: {accent}ff;
    active: {desired_theme["bg3"]}ff;
    urgent: {error}ff;
    }}
    """
    with open(rofi_theme_path, "w") as file:
        file.write(rofi_theme)


def change_vscode_theme(theme):
    vs_theme_name = theme["vscode"]
    shell_command = f'sh ~/.config/qtile/scripts/vscode-theme.sh "{vs_theme_name}"'
    try:
        subprocess.run(shell_command, shell=True, check=True)
        print("Shell script executed successfully.")
    except subprocess.CalledProcessError:
        print("Error occurred while running the shell script.")


def change_theme(theme, accent, error):
    change_vscode_theme(theme)
    write_rofi_theme(theme, accent, error)
    rofi_theme_controller = os.path.expanduser(f"~/.config/qtile/rofi/themes/current_theme.rasi")
    with open(rofi_theme_controller, "w") as file:
        file.write(f'@import "{theme["name"]}"')

