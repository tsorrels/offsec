# Invoke-WebRequest http://192.168.118.2:8081/dnsupdater.ps1 -OutFile dnsupdater.ps1
function Get-IP {
    return Get-NetIPAddress | Where-Object { $_.IPAddress -like '172.16.*' }
}

$third = 50
$octets = ""
while ($third -eq 50) {
    Write-Output "Checking environment..."
    $curr_ip = Get-IP
    $octets = $curr_ip.IPAddress.Split('.')
    $third = $octets[2]
    if ($third -eq 50) {
        Start-Sleep 60
    }
}

$zonename = "dmz.medtech.com"

$Hostname = "web02"
$newobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"
$oldobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"

$localip = (Get-NetIPAddress -InterfaceAlias "Ethernet0").IPAddress
$octet = $localip.Split(".")[2]
$updateip = ($newobj.recorddata.ipv4address.IPAddressToString).split(".")
$updateip[2] = $localip.Split(".")[2]
$updateip = [String]::Join(".", $updateip)
$newobj.recorddata.ipv4address=[System.Net.IPAddress]::parse($updateip)
Set-dnsserverresourcerecord -newinputobject $newobj -oldinputobject $oldobj -zonename $zonename -passthru

$zonename = "medtech.com"

$Hostname = "client01"
$newobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"
$oldobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"

$localip = (Get-NetIPAddress -InterfaceAlias "Ethernet0").IPAddress
$octet = $localip.Split(".")[2]
$updateip = ($newobj.recorddata.ipv4address.IPAddressToString).split(".")
$updateip[2] = $localip.Split(".")[2]
$updateip = [String]::Join(".", $updateip)
$newobj.recorddata.ipv4address=[System.Net.IPAddress]::parse($updateip)
Set-dnsserverresourcerecord -newinputobject $newobj -oldinputobject $oldobj -zonename $zonename -passthru

$Hostname = "client02"
$newobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"
$oldobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"

$localip = (Get-NetIPAddress -InterfaceAlias "Ethernet0").IPAddress
$octet = $localip.Split(".")[2]
$updateip = ($newobj.recorddata.ipv4address.IPAddressToString).split(".")
$updateip[2] = $localip.Split(".")[2]
$updateip = [String]::Join(".", $updateip)
$newobj.recorddata.ipv4address=[System.Net.IPAddress]::parse($updateip)
Set-dnsserverresourcerecord -newinputobject $newobj -oldinputobject $oldobj -zonename $zonename -passthru

$Hostname = "dc01"
$newobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"
$oldobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"

$localip = (Get-NetIPAddress -InterfaceAlias "Ethernet0").IPAddress
$octet = $localip.Split(".")[2]
$updateip = ($newobj.recorddata.ipv4address.IPAddressToString).split(".")
$updateip[2] = $localip.Split(".")[2]
$updateip = [String]::Join(".", $updateip)
$newobj.recorddata.ipv4address=[System.Net.IPAddress]::parse($updateip)
Set-dnsserverresourcerecord -newinputobject $newobj -oldinputobject $oldobj -zonename $zonename -passthru

$Hostname = "dev04"
$newobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"
$oldobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"

$localip = (Get-NetIPAddress -InterfaceAlias "Ethernet0").IPAddress
$octet = $localip.Split(".")[2]
$updateip = ($newobj.recorddata.ipv4address.IPAddressToString).split(".")
$updateip[2] = $localip.Split(".")[2]
$updateip = [String]::Join(".", $updateip)
$newobj.recorddata.ipv4address=[System.Net.IPAddress]::parse($updateip)
Set-dnsserverresourcerecord -newinputobject $newobj -oldinputobject $oldobj -zonename $zonename -passthru

$Hostname = "files02"
$newobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"
$oldobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"

$localip = (Get-NetIPAddress -InterfaceAlias "Ethernet0").IPAddress
$octet = $localip.Split(".")[2]
$updateip = ($newobj.recorddata.ipv4address.IPAddressToString).split(".")
$updateip[2] = $localip.Split(".")[2]
$updateip = [String]::Join(".", $updateip)
$newobj.recorddata.ipv4address=[System.Net.IPAddress]::parse($updateip)
Set-dnsserverresourcerecord -newinputobject $newobj -oldinputobject $oldobj -zonename $zonename -passthru

$Hostname = "prod01"
$newobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"
$oldobj = Get-DnsServerResourceRecord -ZoneName $zonename -Name $Hostname -RRType "A"

$localip = (Get-NetIPAddress -InterfaceAlias "Ethernet0").IPAddress
$octet = $localip.Split(".")[2]
$updateip = ($newobj.recorddata.ipv4address.IPAddressToString).split(".")
$updateip[2] = $localip.Split(".")[2]
$updateip = [String]::Join(".", $updateip)
$newobj.recorddata.ipv4address=[System.Net.IPAddress]::parse($updateip)
Set-dnsserverresourcerecord -newinputobject $newobj -oldinputobject $oldobj -zonename $zonename -passthru

