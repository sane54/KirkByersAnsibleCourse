from snmp_helper import snmp_get_oid, snmp_extract

my_device = ('184.105.247.70', 'galileo', 161)
snmp_data_dump = snmp_get_oid(my_device,  '1.3.6.1.2.1.1.1.0')
print "system description = " + snmp_extract(snmp_data_dump)
snmp_data_dump = snmp_get_oid(my_device,  '1.3.6.1.2.1.1.5.0')
print "hostname = " + snmp_extract(snmp_data_dump)
print ""
my_device = ('184.105.247.71', 'galileo', 161)
snmp_data_dump = snmp_get_oid(my_device,  '1.3.6.1.2.1.1.1.0')
print "system description = " + snmp_extract(snmp_data_dump)
snmp_data_dump = snmp_get_oid(my_device,  '1.3.6.1.2.1.1.5.0')
print "hostname = " + snmp_extract(snmp_data_dump)

