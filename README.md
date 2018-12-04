# SDN
This repository was created in order to demonstrate an implementation of DHCP service on SDN with Mininet and Ryu

# Requirements
- VirtualBox 
- Vagrant 
  - Virtual machine running Ubuntu (Vagrant init ubuntu/xenial64)

Make a directory
$ mkdir MininetVM
$ cd MininetVM
$ vagrant init ubuntu/xenial64

Include these lines inside the Vagrantfile (before the *end*):
config.ssh.forward_agent = true
config.ssh.forward_x11 = true

Start the virtual machine
$ vagrant up

Get into the machine
$ vagrant ssh

Update the machine apt
$ sudo apt update

Install python
$ sudo apt -f -y install python-all python-pip
$ export LC_ALL=C
$ pip install setuptools

Install Mininet
$ git clone https://github.com/mininet/mininet
$ ./mininet/util/install.sh -a

Install Ryu
$ git clone https://github.com/marqueswsm/SDN.git
$ apt-get install zip
$ apt-get install unzip
$ cd SDN
$ unzip ryu.zip
$ cd ryu
$ pip install .
$ cd ryu; pip install .

Disabling IPv6
Create a file named "disableipv6" containing (everything in the same line)
px for h in net.hosts: h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1 && sysctl -w net.ipv6.conf.default.disable_ipv6=1 && sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

Start mininet
- sudo mn --pre=disableipv6

# Tutorial

Firstly, we need install a DHCP service. Then, execute:
```bash
  sudo apt update
  sudo apt install isc-dhcp-server
```

Then, we need to change the dhcpd.conf file:
```bash
  sudo rm /etc/dhcp/dhcpd.conf
  # get the file to copy from this repository
  sudo cp dhcpd.conf /etc/dhcp/
  sudo chmod 777 /etc/dhcp/dhcpd.conf
  sudo chmod 777 /var/lib/dhcp/dhcpd.leases
```

....

Constrution. 

On the h1, execute:
```bash
  dhcpd -f -4 -cf /etc/dhcp/dhcpd.conf
```

On the other hand, on the h3 host, run:
```bash
  hdclient h3-eth0
```


