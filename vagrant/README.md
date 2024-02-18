## window systems:

``` powershell
function fn-powershell {
    $sourceDir = "fn_powershell"
    $currentDir = Get-Location
    $sourcePath = Join-Path -Path $currentDir -ChildPath $sourceDir

    if (Test-Path -Path $sourcePath) {
        $psFiles = Get-ChildItem -Path $sourcePath -Filter *.ps1
        foreach ($file in $psFiles) {
            . $file.FullName
        }
        Write-Host "Sourced all PowerShell files in $sourcePath."
    } else {
        Write-Host "Directory $sourcePath not found."
    }
}
```
- copy and paste the above function to $PROFILE 
    > ```powershell
    > notepad $PROFILE   
    >```
          
- restart the terminal and source the function
    > ```powershell
    > . fn-powershell
    >```

- to skip vagrant provisioners run the below command
    > ```shell
    > . fn-powershell
    > vagrant-skip -p "install_pkgs"
    >```

