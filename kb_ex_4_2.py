#Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.

import paramiko
from time import sleep

ipaddr = '184.105.247.71'
username = 'pyclass'
password = '88newclass'


#create a Paramiko SSH Client object: 

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ipaddr, username = username, password = password, look_for_keys = False, allow_agent = False)

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(5000)
print output

remote_conn.send("config t\n")
sleep(1)
output = remote_conn.recv(5000)
print output

remote_conn.send('logging buffered 4096\n')
sleep(1)
output = remote_conn.recv(5000)
print output

remote_conn.send('exit\n')
sleep(1)
output = remote_conn.recv(5000)
print output

remote_conn.send('terminal length 0\n')
sleep(1)
output = remote_conn.recv(5000)
print output

remote_conn.send('show run\n')
sleep(1)
output = remote_conn.recv(5000)
print output

remote_conn_pre.close()
