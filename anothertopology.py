#!/usr/bin/env python
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link,TCLink,Intf

if '__main__' == __name__:
  net = Mininet(link=TCLink)
  h1 = net.addHost('h1')
  h2 = net.addHost('h2')
  r1 = net.addHost('r1')
  Link(h1, r1, intfName1='h1-eth0', intfName2='r1-eth0')
  Link(h2, r1, intfName1='h2-eth0', intfName2='r1-eth1')
  net.build()
  r1.cmd('ifconfig r1-eth0 192.168.1.1 netmask 255.255.255.0')
  r1.cmd('ifconfig r1-eth1  10.0.0.1 netmask 255.255.255.0')
  r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
  r1.cmd("iptables -t nat -A POSTROUTING -o r1-eth1 -s 192.168.1.0/24 -j MASQUERADE")
  r1.cmd("dhcpd -f -4 -cf /etc/dhcp/dhcpd.conf &")
  h1.cmd("ifconfig h1-eth0 0")
  h1.cmd("dhclient h1-eth0")
  h2.cmd("ifconfig h2-eth0 0")
  h2.cmd("ip addr add 10.0.0.2/24 brd + dev h2-eth0")
  h2.cmd("ip route add default via 10.0.0.1")
  CLI(net)
  net.stop()
