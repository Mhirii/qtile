#!bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <theme>"
    exit 1
fi

theme="$1"

# Make sure to provide the correct path to the settings.json file
settings_file="$HOME/.config/Code - OSS/User/settings.json"

# Use double quotes around the sed expression and escape the double quotes within the expression
sed -i -e "s|\"workbench.colorTheme\": \".*\"|\"workbench.colorTheme\": \"$theme\"|g" "$settings_file"