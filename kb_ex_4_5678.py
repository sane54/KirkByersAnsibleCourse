#Netmiko

import netmiko

#create device dictionaries
pynet_rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22
}

pynet_rtr1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22
}

juniper_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22
}   
    
pynet_rtr2_connect = netmiko.ConnectHandler(**pynet_rtr2)

output  = pynet_rtr2_connect.send_command('show arp')
print output
pynet_rtr2_connect.config_mode()
output = pynet_rtr2_connect.check_config_mode()
print output
pynet_rtr2_connect.send_command('logging buffered 4096')
pynet_rtr2_connect.exit_config_mode()
pynet_rtr2_connect.cleanup()

pynet_rtr1_connect = netmiko.ConnectHandler(**pynet_rtr1)
output  = pynet_rtr1_connect.send_command('show arp')
print output
pynet_rtr1_connect.cleanup()

juniper_srx_connect = netmiko.ConnectHandler(**juniper_srx)
output  = juniper_srx_connect.send_command('show arp')
print output
juniper_srx_connect.cleanup()

pynet_rtr1_connect = netmiko.ConnectHandler(**pynet_rtr1)
pynet_rtr1_connect.send_config_from_file(config_file='configFile.txt')
pynet_rtr1_connect.cleanup()

pynet_rtr2_connect = netmiko.ConnectHandler(**pynet_rtr2)
pynet_rtr2_connect.send_config_from_file(config_file='configFile.txt')
pynet_rtr2_connect.cleanup()

