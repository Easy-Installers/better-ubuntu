import listui
import os
import json

SUDO = "gksudo -- bash -c "
UPDATE = "apt-get update; "
UPGRADE = "apt-get upgrade; "
INSTALL = "apt-get install -y "

def installPackets():
    with open('../packets.json', 'r') as f:
      packets = listui.askDialog("Packets", json.loads(f.read()))
      if len(packets) < 1:
      	return
      packetlist = " ".join(packets)
      install_packets = INSTALL + packetlist
      cmd = SUDO + "'" + UPDATE + UPGRADE + install_packets + "'"
      os.system(cmd)

if __name__ == "__main__":
    import sys
    installPackets()
    sys.exit(0)