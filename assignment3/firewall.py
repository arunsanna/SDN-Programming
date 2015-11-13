'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment: Layer-2 Firewall Application

Developed  from the template of the Software Defined Networking of Dr. Nick
Developed and  Cutomized  by : Mr Arun Sanna
Reasearch Work  EE-598  under Prof. Dong
California State University Los Angeles
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''
import csv


log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]  

''' Add your global variables here ... '''



class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")
        self.deny=[]
        with open(policyFile,'rb') as mycsv:
            reader_macfilter_from_file=csv.DictReader(mycsv)
            for row in reader_macfilter_from_file:
                self.deny.append((EthAddr(row['mac_0']),EthAddr(row['mac_1'])))
                self.deny.append((EthAddr(row['mac_1']),EthAddr(row['mac_0'])))
                

    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        match=of.ofp_match()
        msg=of.ofp_flow_mod()
        for(src,dst)in self.deny:
            #match=of.ofp_match()
            match.dl_src=src
            match.dl_dst=dst
            #msg=of.ofp_flow_mod()
            msg.match=match
            #msg.priority=0x9000
            event.connection.send(msg)
                                 
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
