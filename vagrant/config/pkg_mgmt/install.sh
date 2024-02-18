#!/bin/bash

# # Function to check if a package is installed
# is_installed() {
#     dpkg-query -W -f='${Status}' "$1" 2>/dev/null | grep -q "install ok installed"
# }

# Update package lists
apt-get update

# List of packages to be installed
packages=(
    curl
    bash-completion
    git
    fzf
    jq
)

# # Read packages from file
# packages=()
# while IFS= read -r line; do
#     packages+=("$line")
# done < "/vagrant/config/pkg_mgmt/pkg.txt"

# Install packages only if they are not already installed
for pkg in "${packages[@]}"; do
    echo "Installing $pkg..."
    apt-get install -y --no-install-recommends "$pkg"
done