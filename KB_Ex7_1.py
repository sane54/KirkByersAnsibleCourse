import pyeapi
pynet_sw4 = pyeapi.connect_to('pynet-sw4')
show_int = pynet_sw4.enable('show interfaces')
show_int = show_int[0]
show_int = show_int['result']
show_int = show_int['interfaces']
for intkey in show_int.keys():
    interface = show_int[intkey]
    if 'interfaceCounters' in interface:
        p_counters = interface['interfaceCounters']
        in_octets = p_counters['inOctets']
        out_octets = p_counters['outOctets']
    else:
        in_octets = 0
        out_octets = 0
    if_name = interface['name']
    print if_name, in_octets, out_octets
