#!/bin/bash

#disable apport
sudo sh -c 'echo "# set this to 0 to disable apport, or to 1 to enable it
# you can temporarily override this with
# sudo service apport start force_start=1
enabled=0" >> /etc/default/apport'

# Install ppas and one time-installs
sudo apt-get install -y python-software-properties
sudo add-apt-repository -y ppa:webupd8team/java
sudo add-apt-repository -y ppa:webupd8team/sublime-text-3
sudo add-apt-repository -y ppa:lestcape/cinnamon
sudo add-apt-repository -y ppa:numix/ppa

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886
echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list

wget https://raw.githubusercontent.com/penguinmenac3/better-ubuntu/master/scripts/installers/google-chrome.sh
chmod +x google-chrome.sh
./google-chrome.sh
rm google-chrome.sh

wget https://raw.githubusercontent.com/penguinmenac3/better-ubuntu/master/scripts/installers/ts3.sh
chmod +x ts3.sh
./ts3.sh
rm ts3.sh

wget https://raw.githubusercontent.com/penguinmenac3/better-ubuntu/master/scripts/installers/synology-cloud-station.sh
chmod +x synology-cloud-station.sh
./synology-cloud-station.sh
rm synology-cloud-station.sh

sudo apt-get update
sudo apt-get install -y sublime-text-installer
sudo apt-get install -y oracle-java8-installer

wget https://raw.githubusercontent.com/penguinmenac3/better-ubuntu/master/scripts/update.sh
chmod +x update.sh
./update.sh

rm install.sh