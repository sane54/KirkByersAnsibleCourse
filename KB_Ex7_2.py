#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', action="store", dest="name", help = "vlan name")
parser.add_argument('--remove', action='store_true', default=False, dest="doiremove", help = "remove the vlan")
parser.add_argument('vlan_id', action="store", type=int)
#my_args = parser.parse_args(['--name',  'Jay', '--remove', '228'])
my_args = parser.parse_args()
vlan_id = my_args.vlan_id
name = my_args.name
doiremove = my_args.doiremove
if (vlan_id < 100) or (vlan_id > 999):
    print "choose a vlan id greater than 100 and less than 999"
    exit()
vlan_id =   str(vlan_id)
import pyeapi
pynet_sw4 = pyeapi.connect_to('pynet-sw4')
show_vlan = pynet_sw4.enable('show vlan')
show_vlan = show_vlan[0]
show_vlan = show_vlan['result']
show_vlan = show_vlan['vlans']
if vlan_id not in show_vlan.keys():
    print "vlan id is not in vlan keys so I need to add it"
    cmds = ['vlan ' + vlan_id, 'name ' + name]
    pynet_sw4.config(cmds)
else:
    if doiremove:
        print "I need to remove this vlan"
        cmds = ['no vlan ' + vlan_id]
        pynet_sw4.config(cmds)
    else:
        print "Vlan already exists"
show_vlan = pynet_sw4.enable('show vlan')
show_vlan = show_vlan[0]
show_vlan = show_vlan['result']
show_vlan = show_vlan['vlans']
from pprint import pprint
pprint(show_vlan)
