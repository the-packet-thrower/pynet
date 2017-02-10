import paramiko
from getpass import getpass


username = 'pyclass'
pynet_rtr1 = '184.105.247.70'
pynet_rtr2 = '184.105.247.71'
username = 'pyclass'
password = '88newclass'

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre
#Auto Add SSH host keys
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#Can also use: "remote_conn_pre.load_system_host_keys()" to load system keys


remote_conn_pre.connect(pynet_rtr1, username=username, password=password, look_for_keys=False, allow_agent=False)
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(5000)

print output
pynet-rtr1#

remote_conn.send("show ip int br\n")
15

output = remote_conn.recv(5000)

print output
show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0              unassigned      YES unset  down                  down    
FastEthernet1              unassigned      YES unset  down                  down    
FastEthernet2              unassigned      YES unset  down                  down    
FastEthernet3              unassigned      YES unset  down                  down    
FastEthernet4              10.220.88.20    YES NVRAM  up                    up      
Vlan1                      unassigned      YES unset  down                  down    
pynet-rtr1#
