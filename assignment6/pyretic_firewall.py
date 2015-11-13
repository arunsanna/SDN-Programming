'''
Developed  from the template of the Software Defined Networking of Dr. Nick
Developed and  Cutomized  by : Mr Arun Sanna
Reasearch Work  EE-598  under Prof. Dong
California State University Los Angeles

'''''

################################################################################
# The Pyretic Project                                                          #
# frenetic-lang.org/pyretic                                                    #
# author: Joshua Reich (jreich@cs.princeton.edu)                               #
################################################################################
# Licensed to the Pyretic Project by one or more contributors. See the         #
# NOTICES file distributed with this work for additional information           #
# regarding copyright and ownership. The Pyretic Project licenses this         #
# file to you under the following license.                                     #
#                                                                              #
# Redistribution and use in source and binary forms, with or without           #
# modification, are permitted provided the following conditions are met:       #
# - Redistributions of source code must retain the above copyright             #
#   notice, this list of conditions and the following disclaimer.              #
# - Redistributions in binary form must reproduce the above copyright          #
#   notice, this list of conditions and the following disclaimer in            #
#   the documentation or other materials provided with the distribution.       #
# - The names of the copyright holds and contributors may not be used to       #
#   endorse or promote products derived from this work without specific        #
#   prior written permission.                                                  #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT    #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the     #
# LICENSE file distributed with this work for specific language governing      #
# permissions and limitations under the License.                               #
################################################################################

from pyretic.lib.corelib import *
from pyretic.lib.std import *

from pyretic.modules.mac_learner import mac_learner
import os
import csv
from pox.lib.addresses import EthAddr
from collections import namedtuple
# insert the name of the module and policy you want to import
#from pyretic.examples.<....> import <....>
policy_file = "%s/pyretic/pyretic/examples/firewall-policies.csv" % os.environ[ 'HOME' ]

def main():
    # Copy the code you used to read firewall-policies.csv from the Pox Firewall assignment
    
    not_allowed=none
    with open(policy_file,'rb') as mycsv:
        reader_macfilter_from_file=csv.DictReader(mycsv)
        for row in reader_macfilter_from_file:
            ssssssss

            not_allowed = union( [not_allowed,union( [match(srcmac=MAC(row['mac_0']),
                                                             dstmac=MAC(row['mac_1'])
                                                             ),
                                                      match(srcmac=MAC(row['mac_1']),
                                                            dstmac=MAC(row['mac_0']))
                                                      ]
                                                     )
                                  ]
                                 )

    # start with a policy that doesn't match any packets
    
    
    # and add traffic that isn't allowed
    
    # express allowed traffic in terms of not_allowed - hint use '~'
    allowed = ~not_allowed
                                             
    #print "not_allowed : "
    #print not_allowed
    #print "allowed :"
    #print allowed
    # and only send allowed traffic to the mac learning (act_like_switch) logic
    return allowed >> mac_learner()



