# SDN
This repository was created in order to demonstrate an implementation of DHCP service on SDN with Mininet and Ryu

# Requirements
- VirtualBox 
- Vagrant 
  - Virtual machine running Ubuntu (Vagrant init ubuntu/xenial64)

Make a directory
```
$ mkdir MininetVM
$ cd MininetVM
$ vagrant init ubuntu/xenial64
```

Include these lines inside the Vagrantfile (before the *end*):
config.ssh.forward_agent = true
config.ssh.forward_x11 = true

Start the virtual machine
```
$ vagrant up
```

Get inside the machine
```
$ vagrant ssh
```

Update the machine apt
```
$ sudo apt update
```

Install python
```
$ sudo apt -f -y install python-all python-pip
$ export LC_ALL=C
$ pip install setuptools
```

Install Mininet
```
$ git clone https://github.com/mininet/mininet
$ ./mininet/util/install.sh -a
```

Install Ryu
```
$ git clone https://github.com/marqueswsm/SDN.git
$ apt-get install zip
$ apt-get install unzip
$ cd SDN
$ unzip ryu.zip
$ cd ryu
$ pip install .
$ cd ryu; pip install .
```

Disabling IPv6
Create a file named "disableipv6" containing (everything in the same line)
px for h in net.hosts: h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1 && sysctl -w net.ipv6.conf.default.disable_ipv6=1 && sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

Start mininet
- sudo mn --pre=disableipv6

# Tutorial

Firstly, we need to install a DHCP service. To do that, you have to execute:
```bash
  sudo apt update
  sudo apt install isc-dhcp-server
```

# Executing the attack

First it is necessary to build the topology, be sure that you are inside the SDN folder:
```
$ sudo python topology.py
```
After that you need to open one of the nodes that were created by the topology and start the attack:
```
$ xterm h2
$ sudo python ataque.py
```

