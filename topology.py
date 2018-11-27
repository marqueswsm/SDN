#!/usr/bin/python
"""
    Script created by waguininho das gurias
"""
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
def topology():
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )
    c1 = net.addController( 'c1', controller=RemoteController, ip='127.0.0.1', port=6633 )
    s2 = net.addSwitch( 's2', listenPort=6634, mac='00:00:00:00:00:01' )
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:03', ip='192.168.1.100/24' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:04', ip='192.168.1.101/24' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:05', ip='no ip/24' )
    # for h in net.hosts: h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1 && sysctl -w net.ipv6.conf.default.disable_ipv6=1 && sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
    net.addLink(h1, s2)
    net.addLink(h2, s2)
    net.addLink(h3, s2)
    net.build()
    s2.start([c1])
    c1.start()
    h1.cmd("sudo rm /etc/dhcp/dhcpd.conf")
    h1.cmd("sudo cp dhcpd.conf /etc/dhcp/dhcpd.conf")
    h1.cmd("sudo chmod 777 /etc/dhcp/dhcpd.conf")
    h1.cmd("sudo chmod 777 /var/lib/dhcp/dhcpd.leases")
    h1.cmd("dhcpd -f -4 -cf /etc/dhcp/dhcpd.conf &")
    # h3.cmd("dhclient h3-eth0")
    CLI( net )
    net.stop()
if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
# sudo python topology.py