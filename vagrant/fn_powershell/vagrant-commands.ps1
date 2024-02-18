# Vagrant commands
function vagre {
    param(
        [string[]]$p
    )
    $provisionWith = $p -join ","
    vagrant reload --provision-with $provisionWith
}

function reload-bashrc {
    vagre -p "reload_bashrc"
}

function vagrant-up() {
    vagrant up --provsion-with "install_pkgs","install_docker","install_nvm_yarn","set_timezone","ssh_keygen","reload_bashrc"
}

function vnp {
    vagrant up --no-provision
}

function vagrant-up() {
    python .\fn_powershell\vagrant_skip.py -p "remove_pkgs"
}