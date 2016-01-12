import os
import json

SUDO = "sudo -- bash -c "

def installPackets():
    with open('../installers.json', 'r') as f:
      packets = json.loads(f.read())
      if len(packets) < 1:
        return
      installercalls = ""
      for packet in packets:
        if "checked" in packet and packet["checked"]:
      	  installercalls += packet["packet"] + ".sh; "
      cmd = SUDO + "'apt-get install -y python-software-properties; " + installercalls + "'"
      print(cmd)
      os.system(cmd)

if __name__ == "__main__":
    import sys
    installPackets()
    sys.exit(0)