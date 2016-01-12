import listui
import os
import json

SUDO = "gksudo -- bash -c "

def installPackets():
    with open('../installers.json', 'r') as f:
      packets = listui.askDialog("Install", json.loads(f.read()))
      if len(packets) < 1:
        return
      installercalls = ""
      for packet in packets:
      	installercalls += packet + ".sh; "
      cmd = SUDO + "'apt-get install -y python-software-properties; " + installercalls + "'"
      os.system(cmd)

if __name__ == "__main__":
    import sys
    installPackets()
    sys.exit(0)