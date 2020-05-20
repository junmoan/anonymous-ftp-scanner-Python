# -*- coding: utf-8 -*-
# Import.
import ftplib, time

def anonLogin(hostname):
  try:
    ftp = ftplib.FTP(hostname)
    ftp.login("anonymous", "me@your.com")
    print("\n[*] " + str(hostname) + " FTP Anonymous Logon Succeded.")
    ftp.quit()
    #return True
    
  except:
    print("\n[-] " + str(hostname) + " FTP Anonymous Logon Failed.")
    #return False

# Set the IP address and scan an anonymous FTP server.
host = '192.168.130.133'
anonLogin(host)

def ipRange(start_ip, end_ip):
   global ip_range
   start = list(map(int, start_ip.split(".")))
   end = list(map(int, end_ip.split(".")))
   temp = start
   ip_range = []
   ip_range.append(start_ip)
   while temp != end:
      start[3] += 1
      for i in (3, 2, 1):
         if temp[i] == 256:
            temp[i] = 0
            temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))    
   return ip_range

# Set the range of IP address for scanning.
ipList = ipRange('192.168.95.1', '192.168.95.10')
ipList

# Scan anonymous FTP servers.
for i in range(len(ipList)):
    anonLogin(ipList[i])

