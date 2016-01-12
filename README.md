# Better Ubuntu

Initialisation scripts and tools that make your ubuntu better.

This is a project that aims to provide some easy to install tools for ubuntu. These tools are build ontop of ubuntu and assume that you have a clean install to start with.

# How to install with ui configuration

Download the zip. Extract it and start the install_graphical.sh

```bash
wget https://github.com/penguinmenac3/better-ubuntu/archive/master.zip
unzip master.zip
mv better-ubuntu-master better-ubuntu
cd better-ubuntu
./install_graphical.sh
```

Follow the instructions.

![Follow the instructions install](https://raw.githubusercontent.com/penguinmenac3/better-ubuntu/master/images/install-ui.png)

![Follow the instructions packages](https://raw.githubusercontent.com/penguinmenac3/better-ubuntu/master/images/packages-ui.png)

# How to install without configuration

Download the zip. Extract it and start the install_console.sh
```bash
wget https://github.com/penguinmenac3/better-ubuntu/archive/master.zip
unzip master.zip
mv better-ubuntu-master better-ubuntu
cd better-ubuntu
./install_console.sh
```

It will install all packages listed in packets.json and installers.json with the checked attribute true.

![Console autoinstall](https://raw.githubusercontent.com/penguinmenac3/better-ubuntu/master/images/console.png)
