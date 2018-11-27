from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet
from ryu.lib.packet import arp
from ryu.lib.packet import dhcp

class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        dp = msg.datapath
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser
        
        
        pkt = packet.Packet(msg.data)
        dhcpPacket = pkt.get_protocols(dhcp.dhcp)
        if dhcpPacket:
            # print dhcpPacket
            print "dhcpPacket.chaddr ", dhcpPacket[0].chaddr
            if dhcpPacket[0].chaddr != '00:00:00:00:00:05':
                print "Not valid. Discarding packet.\n"
            else:
                print "It's valid. Saving packet.\n"
                actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]
                out = ofp_parser.OFPPacketOut(datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port, actions=actions)
                dp.send_msg(out)
        else:
            print "It's not a DHCP packet."
            actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]
            out = ofp_parser.OFPPacketOut(datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port, actions=actions)
            dp.send_msg(out)


# ryu-manager ryuapplication.py
# DHCP.PY SOURCE: https://raw.githubusercontent.com/Ryuretic/RyureticLabs/master/ryu/ryu/app/Ryuretic/Support_Files/dhcp.py
# LOCALES ERROR FIX: https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting
    # export LC_ALL="en_US.UTF-8"
    # export LC_CTYPE="en_US.UTF-8"
    # sudo dpkg-reconfigure locales

