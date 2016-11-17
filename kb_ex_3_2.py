from snmp_helper import snmp_extract, snmp_get_oid_v3
import time

snmp_user = ('pysnmp', 'galileo1', 'galileo1')
snmp_device = ('184.105.247.70', 161)


snmp_data  = snmp_get_oid_v3(snmp_device, snmp_user, '1.3.6.1.2.1.2.2.1.2.5', 'sha','aes128', True)
fa4_desc = snmp_extract(snmp_data)



#Step 1 - get the following OIDs every 5 minutes
oids = [
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
]

fa4_in_octets = []
fa4_in_packets = []
fa4_out_octets = []
fa4_out_packets = []

for x in range(0, 2):
    fa4_in_octets.append(int(snmp_extract(snmp_get_oid_v3(snmp_device, snmp_user, oids[0][1], 'sha', 'aes128', True))))
    fa4_in_packets.append(int(snmp_extract(snmp_get_oid_v3(snmp_device, snmp_user, oids[1][1], 'sha', 'aes128', True))))
    fa4_out_octets.append(int(snmp_extract(snmp_get_oid_v3(snmp_device, snmp_user, oids[2][1], 'sha', 'aes128', True))))
    fa4_out_packets.append(int(snmp_extract(snmp_get_oid_v3(snmp_device, snmp_user, oids[3][1], 'sha', 'aes128', True))))

    time.sleep(5)

import pygal

# Create a Chart of type Line
line_chart = pygal.Line()

# Title
line_chart.title = fa4_desc + 'Input/Output Packets and Bytes'

# X-axis labels (samples were every five minutes)
line_chart.x_labels = ['5', '10']

# Add each one of the above lists into the graph as a line with corresponding label
line_chart.add('InPackets', fa4_in_packets)
line_chart.add('OutPackets',  fa4_out_packets)
line_chart.add('InBytes', fa4_out_octets)
line_chart.add('OutBytes', fa4_in_octets)

# Create an output image file from this
line_chart.render_to_file('test.svg')
