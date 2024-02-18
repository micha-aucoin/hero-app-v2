import argparse
import subprocess
import re
import os


def skip_provisioners(to_skip: list) -> list:
    python_file_path, _ = os.path.split(__file__)
    vagrant_file_path = os.path.join(os.path.dirname(python_file_path), 'Vagrantfile')
    provisioner_names = []

    with open(vagrant_file_path, 'r') as file:
        content = file.read()

    matches = re.findall(r'config.vm.provision\s+"([^"]+)"', content)
    for match in matches:
        provisioner_names.append(match)

    return [p for p in provisioner_names if p not in to_skip]

def vagrant_provision_with(provision_with):
    # Check if the Vagrant machine is already up and running
    status_output = subprocess.run(["vagrant", "status", "--machine-readable"], capture_output=True, text=True)
    if ",state,running" in status_output.stdout:
        print("Reloading Vagrant machine with new provisioners...")
        provision_command = ["vagrant", "reload", "--provision-with", provision_with]
    else:
        print("Starting Vagrant machine with new provisioners...")
        provision_command = ["vagrant", "up", "--provision-with", provision_with]

    # Execute the Vagrant command
    subprocess.run(provision_command, check=True)

def main():
    parser = argparse.ArgumentParser(description='provide provisioners to skip')
    parser.add_argument('--provision_skip', '-p', type=str, help='Provisioners to skip as a comma-separated string')

    args = parser.parse_args()

    if args.provision_skip:
        provisioners_to_skip = args.provision_skip.split(',')
        provisioners_to_apply = skip_provisioners(provisioners_to_skip)
    
    if provisioners_to_apply:
        provisioners_string = ",".join(provisioners_to_apply)
        vagrant_provision_with(provisioners_string)
    else:
        print("No provisioners to apply.")

if __name__ == "__main__":
    main()
