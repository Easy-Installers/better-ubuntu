import os
import json

SUDO = "sudo -- bash -c "
UPDATE = "apt-get update; "
UPGRADE = "apt-get upgrade; "
INSTALL = "apt-get install -y "

def installPackets():
    with open('../packets.json', 'r') as f:
      packets = json.loads(f.read())
      if len(packets) < 1:
      	return
      packetlist = ""
      for packet in packets:
        if "checked" in packet and packet["checked"]:
          packetlist += packet["packet"] + " "
      install_packets = INSTALL + packetlist
      cmd = SUDO + "'" + UPDATE + UPGRADE + install_packets + "'"
      print(cmd)
      os.system(cmd)

if __name__ == "__main__":
    import sys
    installPackets()
    sys.exit(0)