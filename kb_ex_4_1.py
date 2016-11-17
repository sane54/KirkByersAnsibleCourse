#Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2. 

import paramiko
from getpass import getpass
from time import sleep

ipaddr = '184.105.247.71'
username = 'pyclass'
#password = getpass()
password = '88newclass'
port = 22

#create a Paramiko SSH Client object: 

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ipaddr, username = username, password = password, look_for_keys = False, allow_agent = False)

remote_conn = remote_conn_pre.invoke_shell() #On a cisco device if you don't do this it will tear down after a single command
#output = remote_conn.recv(1000)
#print output

remote_conn.send('terminal length 0\n')
#sleep(1)
#output = remote_conn.recv(1000)
#print output

remote_conn.send("show version\n")
sleep(3)
output = remote_conn.recv(5000)
print output
remote_conn_pre.close()
