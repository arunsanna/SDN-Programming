'''
Developed  from the template of the Software Defined Networking of Dr. Nick
Developed and  Cutomized  by : Mr Arun Sanna
Reasearch Work  EE-598  under Prof. Dong
California State University Los Angeles

'''

from pox.core import core
from collections import defaultdict

import pox.openflow.libopenflow_01 as of
import pox.openflow.discovery
import pox.openflow.spanning_tree

from pox.lib.revent import *
from pox.lib.util import dpid_to_str
from pox.lib.util import dpidToStr
from pox.lib.addresses import IPAddr, EthAddr
from collections import namedtuple
import os

log = core.getLogger()


class TopologySlice (EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Slicing Module")
        
        
    """This event will be raised each time a switch will connect to the controller"""
    def _handle_ConnectionUp(self, event):
        
        # Use dpid to differentiate between switches (datapath-id)
        # Each switch has its own flow table. As we'll see in this 
        # example we need to write different rules in different tables.
        dpid = dpidToStr(event.dpid)
        log.debug("Switch %s has come up.", dpid)
        
        """ Add your logic here """
       
        
        print("*********")
        print dpid
        #core.openflow.sendToDPID()

        #=======================#
        #  SWITCH 1 or SWITCH 4 #
        #=======================#

        # if a packet is inport = 3, outport = 1
        # if a packet is inport = 4, outport = 2

        if dpid[-2:] in ("01" , "04"):
            
            # if a packet is inport = 3, outport = 1
            print "SWITCH %s CONNECTED " % str(dpid[-2:])
            upper_slice = of.ofp_flow_mod()
            upper_slice.match.in_port = 3
            upper_slice.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(upper_slice)
            
            # above bi-dir
            upper_slice_bi = of.ofp_flow_mod()
            upper_slice_bi.match.in_port = 1
            upper_slice_bi.actions.append(of.ofp_action_output(port = 3))
            event.connection.send(upper_slice_bi)
            
            # if a packet is inport = 4, outport = 2
            lower_slice = of.ofp_flow_mod()
            lower_slice.match.in_port = 4
            lower_slice.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(lower_slice)

            # above bi-dir
            lower_slice_bi = of.ofp_flow_mod()
            lower_slice_bi.match.in_port = 2
            lower_slice_bi.actions.append(of.ofp_action_output(port = 4))
            event.connection.send(lower_slice_bi)
            


        #======================#
        # SWITCH 2 or SWITCH 3 # 
        #======================#
            
        # if a packet is inport = 1, outport = 2

        elif dpid[-2:] in ("02" , "03"):
            print "SWITCH %s CONNECTED " % str(dpid[-2:])
            slice_msg = of.ofp_flow_mod()
        
            slice_msg.match.in_port = 1
            slice_msg.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(slice_msg)
           # Above bi-dir
 
            slice_msg_bi = of.ofp_flow_mod()
            slice_msg_bi.match.in_port = 2
            slice_msg_bi.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(slice_msg_bi)
            
           

        

def launch():
    # Run spanning tree so that we can deal with topologies with loops
    pox.openflow.discovery.launch()
    pox.openflow.spanning_tree.launch()

    '''
    Starting the Topology Slicing module
    '''
    core.registerNew(TopologySlice)
