#!bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <theme>"
    exit 1
fi

theme="$1"

# Make sure to provide the correct path to the settings.json file
settings_file="$HOME/.config/Code - OSS/User/settings.json"
settings_file1="$HOME/.config/Code - OSS/User/profiles/75cb845f/settings.json"
settings_file2="$HOME/.config/Code - OSS/User/profiles/-524f0689/settings.json"
settings_file3="$HOME/.config/Code - OSS/User/profiles/-7a32e568/settings.json"

# Use double quotes around the sed expression and escape the double quotes within the expression
sed -i -e "s|\"workbench.colorTheme\": \".*\"|\"workbench.colorTheme\": \"$theme\"|g" "$settings_file"
sed -i -e "s|\"workbench.colorTheme\": \".*\"|\"workbench.colorTheme\": \"$theme\"|g" "$settings_file1"
sed -i -e "s|\"workbench.colorTheme\": \".*\"|\"workbench.colorTheme\": \"$theme\"|g" "$settings_file2"
sed -i -e "s|\"workbench.colorTheme\": \".*\"|\"workbench.colorTheme\": \"$theme\"|g" "$settings_file3"