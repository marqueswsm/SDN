# SDN
This repository was created in order to present an implementation of DHCP service on SDN with Mininet and Ryu

# Requirements

- VirtualBox 
- Vagrant 
  - Virtual machine running Ubuntu (Vagrant init ubuntu/xenial64)

# Tutorial

Firstly, we need install a DHCP service. Then, execute:
```bash
  sudo apt update
  sudo apt install isc-dhcp-server
```

Then, we need to alter the dhcpd.conf file:
```bash
  sudo rm /etc/dhcp/dhcpd.conf
  # get the file to copy from this repository
  sudo cp dhcpd.conf /etc/dhcp/
  sudo chmod 777 /etc/dhcp/dhcpd.conf
```

....

Constrution. 


