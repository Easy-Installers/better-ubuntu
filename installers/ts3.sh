#!/bin/bash

wget http://dl.4players.de/ts/releases/3.0.18.2/TeamSpeak3-Client-linux_amd64-3.0.18.2.run
chmod +x TeamSpeak3-Client-linux_amd64-3.0.18.2.run
./TeamSpeak3-Client-linux_amd64-3.0.18.2.run
rm TeamSpeak3-Client-linux_amd64-3.0.18.2.run

sudo mv TeamSpeak3-Client-linux_amd64 /opt/teamspeak3

sudo sh -c "echo '[Desktop Entry]
Type=Application
Name=Teamspeak 3 Client
GenericName=Teamspeak
Comment=Speak with friends
Comment[de]=Spreche mit Freunden
Exec=/opt/teamspeak3/ts3client_runscript.sh
Icon=/opt/teamspeak3/pluginsdk/docs/client_html/images/logo.png
Terminal=false
X-MultipleArgs=false
Categories=Network
StartupWMClass=Teamspeak
StartupNotify=true' >> /usr/share/applications/ts3.desktop"
