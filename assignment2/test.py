'''
Developed  from the template of the Software Defined Networking of Dr. Nick
Developed and  Cutomized  by : Mr Arun Sanna
Reasearch Work  EE-598  under Prof. Dong
California State University Los Angeles

'''
#!/usr/bin/python

from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from CustomTopo import *


if __name__=='__main__':
    setLogLevel('info')
    linkopts1 = {'bw':50, 'delay':'5ms'}
    linkopts2 = {'bw':30, 'delay':'10ms'}
    linkopts3 = {'bw':10, 'delay':'15ms'}

    topo = CustomTopo(linkopts1, linkopts2, linkopts3, fanout=2)
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    net.pingAll()
    dumpNodeConnections(net.hosts)
    net.stop()
