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

    r1 = net.addHost( 'r1', mac='00:00:00:00:00:03', ip='no ip/24' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:04', ip='no ip/24' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:05', ip='no ip/24' )

    net.addLink(r1, s2)
    net.addLink(h2, s2)
    net.addLink(h3, s2)

    r1.cmd('ifconfig r1-eth0 192.168.1.1 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth1  10.0.0.1 netmask 255.255.255.0')
    r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    r1.cmd("iptables -t nat -A POSTROUTING -o r1-eth1 -s 192.168.1.0/24 -j MASQUERADE")
    r1.cmd("dhcpd -f -4 -cf /etc/dhcp/dhcpd.conf &")

    net.build()
    s2.start([c1])
    c1.start()

    CLI( net )

    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
