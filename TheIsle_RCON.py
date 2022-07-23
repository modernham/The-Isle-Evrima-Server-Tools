import socket, time, sys
import os

ip = "127.0.0.1"
port = 8888
password = "password"
timeout = 5
packetMainLength = 2


def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def saveServer():
  cls()
  SAVE = bytes('\x02', 'utf-8') + bytes('\x50', 'utf-8') + bytes('\x00', 'utf-8')
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the TCP Socket
    s.settimeout(timeout)
    s.connect((ip, port))
    s.send((SAVE))

def makeAnouncment():
  cls()
  userinput = input("Please enter the message: ")
  ANOUNCE =  bytes('\x02', 'utf-8') + bytes('\x10', 'utf-8') + userinput.encode() + bytes('\x00', 'utf-8')
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the TCP Socket
    s.settimeout(timeout)
    s.connect((ip, port))
    s.send((ANOUNCE))

def banPlayer():
  cls()
  print("Format: [SteamID(BASE64)], [description], [ban length in seconds(0 is Permanent)]")
  userinput = input("Please enter ban info in the format above: ")
  BAN =  bytes('\x02', 'utf-8') + bytes('\x20', 'utf-8') + userinput.encode() + bytes('\x00', 'utf-8')
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the TCP Socket
    s.settimeout(timeout)
    s.connect((ip, port))
    s.send((BAN))

def kickPlayer():
  cls()
  userinput = input("Please enter the player ID to kick(SteamID in Base64): ")
  KICK =  bytes('\x02', 'utf-8') + bytes('\x30', 'utf-8') + userinput.encode() + bytes('\x00', 'utf-8')
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the TCP Socket
    s.settimeout(timeout)
    s.connect((ip, port))
    s.send((KICK))

def playerList():
  cls()
  LIST =  bytes('\x02', 'utf-8') + bytes('\x40', 'utf-8') + bytes('\x00', 'utf-8')
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the TCP Socket
    s.settimeout(timeout)
    s.connect((ip, port))
    s.send((LIST))
    message = s.recv(1024)
    print("Server returned: " + str(message.decode()))
    input("Press Enter to continue")

def chooseCommand():
  cls()
  print("Credit: Aspect#3735")
  print("Version: 0.1")
  while True:
    print("Please select one of the below support commands")
    print("1 - Save the Server")
    print("2 - Make an Announcement")
    print("3 - Ban a Player")
    print("4 - Kick a Player")
    print("5 - Display Player List")
    print("6 - Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
      saveServer()
    if(choice == 2):
      makeAnouncment()
    if(choice == 3):
      banPlayer()
    if(choice == 4):
      kickPlayer()
    if(choice == 5):
      playerList()
    if(choice == 6):
      sys.exit()


def connect():
  global ip
  global port
  global password
  ip = input("Please enter host IP, Example 155.11.23.55: ")
  port = int(input("Please enter RCON port: "))
  password = input("Please enter RCON password: ")
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Connect to the TCP Socket
    s.settimeout(timeout)
    s.connect((ip, port))
    print("TCP connection established with server")
    #Form our login Packet
    password = password.encode()
    payload = bytes('\x01', 'utf-8') + password + bytes('\x00', 'utf-8')
    print("Sending: "+ str(payload) + "\n")
    s.send((payload))
    message = s.recv(1024)
    if(str(message).__contains__("Accepted")):
      print(message)
    else:
      print("Error")
      sys.exit()
    chooseCommand()


connect()