# -*- coding: utf-8 -*-

# Import.
import ftplib, time
import threading


def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login("anonymous", "test@test.com")
		print("\n[*] " + str(hostname) + " FTP Anonymous Logon Succeded.")
		ftp.quit()
		return True    
	except:
		#print("\n[-] " + str(hostname) + " FTP Anonymous Logon Failed.")
		return False    


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
    

# Set the IP address and scan an anonymous FTP server.
#host = '194.97.2.69'
#anonLogin(host)


# Set the range of the IP addresses.
ipList = ipRange('192.168.40.1', '192.168.40.10')
#ipList = ipRange('213.131.1.1', '213.131.1.255')
print(len(ipList))


# Print the IP addresses FTP servers) allowing Anonymous Login.
for i in range(len(ipList)):
	t = threading.Thread(target=anonLogin, args=(ipList[i],))
	t.start()