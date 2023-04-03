### The Isle RCON Client

---

![Alt text](/RCON_Screenshot.png?raw=true "Screenshot")

Run with:

```bash
python TheIsle_RCON.py
```
Run via command-line arguments (without the brackets)

```bash
#From Python
python TheIsle_RCON.py --ip <IP> --port <PORT> --password <PASSWORD> --command <COMMAND> --args <"COMMAND ARGS">
#From Windows
./TheIsle_RCON.exe --ip <IP> --port <PORT> --password <PASSWORD> --command <COMMAND> --args <"COMMAND ARGS">
```

Examples
```
#Save Server
./TheIsle_RCON.exe --ip 127.0.0.1 --port 8888 --password password123 --command save
#List Players
./TheIsle_RCON.exe --ip 127.0.0.1 --port 8888 --password password123 --command list
#Make Announcement
./TheIsle_RCON.exe --ip 127.0.0.1 --port 8888 --password password123 --command announce --arg "Test Message"
#Ban Player
./TheIsle_RCON.exe --ip 127.0.0.1 --port 8888 --password password123 --command ban --arg "4124125126562541511"
#Kick Player
./TheIsle_RCON.exe --ip 127.0.0.1 --port 8888 --password password123 --command kick --arg "4124125126562541511"
```
### Working Startup commands:

Linux

```bash
TheIsleServer.sh MultiHome=192.181.104.13?Port=7777?QueryPort=7778 -log
```

Windows:

```bash
TheIsleServer.exe MultiHome=192.181.104.13?Port=7777?QueryPort=7778 -log
```

### **Important Note!**

**RCON is unencrypted and passwords are sent in plaintext over the network. BE very careful about using RCON outside of the servers network.** 

### Setup your own Linux Dedicated server!:

https://takethebait.net/create-a-dedicated-the-isle-evrima-server-on-ubuntu-22-04-linux/

### Troubleshoot issues:
https://takethebait.net/troubleshooting-the-isle-dedicated-server-issues/
