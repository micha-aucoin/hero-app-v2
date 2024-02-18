#!/bin/bash

# # Function to check if a package is installed
# is_installed() {
#     dpkg -l "$1" &> /dev/null
# }

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

# Uninstall packages only if they are installed
for pkg in "${packages[@]}"; do
    echo "Uninstalling $pkg..."
    apt-get remove --purge -y "$pkg"
done

# Optional: Autoremove to remove any unused dependencies
apt-get autoremove -y

# Optional: Clean up the local repository of retrieved package files
apt-get clean
