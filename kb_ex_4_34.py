import pexpect
from time import sleep
import sys

ipaddr = '184.105.247.71'
username = 'pyclass'
port = 22
password = '88newclass'
ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ipaddr, port)) # this spawns a child process
ssh_conn.timeout = 3
#ssh_conn.logfile = sys.stdout
ssh_conn.expect("ssword:")
ssh_conn.sendline(password) # note that sendine automatically adds the new line
ssh_conn.expect("pynet-rtr2#")
ssh_conn.sendline('terminal length 0')
ssh_conn.expect("pynet-rtr2#")
ssh_conn.sendline('show ip int brief')
sleep(1)
ssh_conn.expect("pynet-rtr2#")
print ssh_conn.before
ssh_conn.sendline('config t')
ssh_conn.expect("\(config\)#")
ssh_conn.sendline('logging buffered 4096')
ssh_conn.expect("\(config\)#")
ssh_conn.sendline('exit')
ssh_conn.expect("#")
ssh_conn.sendline('show run | inc log ')
ssh_conn.expect("pynet-rtr2#")
print ssh_conn.before
ssh_conn.close()
