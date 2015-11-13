'''
Developed  from the template of the Software Defined Networking of Dr. Nick
Developed and  Cutomized  by : Mr Arun Sanna
Reasearch Work  EE-598  under Prof. Dong
California State University Los Angeles

'''
from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        self.linkopts1=linkopts1
        self.linkopts2=linkopts2
        self.linkopts3=linkopts3
        # Add your logic here ...
        # Numbering:  h1..N, s1..M
        self.hostNum = 1
        self.switchNum = 1
        self.depth=3
        # Build topology
        self.addTree( self.depth, fanout, linkopts1, linkopts2, linkopts3 )
        

    def addTree( self, depth, fanout, linkopts1, linkopts2, linkopts3 ):
        """Add a subtree starting with node n.
           returns: last node added"""
        isSwitch = depth > 0
        if isSwitch:
            node = self.addSwitch( 's%s' % self.switchNum )
            self.switchNum += 1
            for _ in range( fanout ):
                child = self.addTree( depth - 1, fanout , linkopts1, linkopts2, linkopts3)
                # linkopts1: for specifying performance parameters for the links between core and aggregation switches.
                if depth==1:
                    print " in depth 1"
                    self.addLink( node, child ,**linkopts1)
                # linkopts2: for specifying performance parameters for the links between aggregation and edge switches.
                if depth==2:
                    print " in depth 2"
                    self.addLink( node, child ,**linkopts2)
                # linkopts3: for specifying performance parameters for the links between edge switches and host
                if depth==3:
                    print " in depth 3"
                    self.addLink( node, child ,**linkopts3)
        else:
            node = self.addHost( 'h%s' % self.hostNum )
            self.hostNum += 1
        return node
    
        
                    
topos = { 'custom': ( lambda: CustomTopo() ) }
'''
from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        self.linkopts1=linkopts1
        self.linkopts2=linkopts2
        self.linkopts3=linkopts3
        # Add your logic here ...
        # Numbering:  h1..N, s1..M
        self.hostNum = 1
        self.switchNum = 1
        self.depth=3
        # Build topology
        self.addTree( self.depth, fanout)
        

    def addTree( self, depth, fanout):
        """Add a subtree starting with node n.
           returns: last node added"""
        isSwitch = depth > 0
        if isSwitch:
            node = self.addSwitch( 's%s' % self.switchNum )
            self.switchNum += 1
            for _ in range( fanout ):
                child = self.addTree( depth - 1, fanout )
                # linkopts1: for specifying performance parameters for the links between core and aggregation switches.
                if depth==1:
                    print " in depth 1"
                    self.addLink( node, child ,**self.linkopts3)
                # linkopts2: for specifying performance parameters for the links between aggregation and edge switches.
                if depth==2:
                    print " in depth 2"
                    self.addLink( node, child ,**self.linkopts2)
                # linkopts3: for specifying performance parameters for the links between edge switches and host
                if depth==3:
                    print " in depth 3"
                    self.addLink( node, child ,**self.linkopts1)
        else:
            node = self.addHost( 'h%s' % self.hostNum )
            self.hostNum += 1
        return node
    
        
                    
topos = { 'custom': ( lambda: CustomTopo() ) }
