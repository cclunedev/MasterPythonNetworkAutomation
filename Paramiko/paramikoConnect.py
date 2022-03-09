import paramiko

sshClient = paramiko.SSHClient()

print(type(sshClient))

sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
r1 = {'hostname': '192.168.122.10', 'port':'22', 'username': 'admin', 'password': 'cisco'}

print(f'Connecting to {r1["hostname"]}')

#sshClient.connect(hostname='192.168.122.10', port='22', username='admin', password='cisco', look_for_keys=False, allow_agent=False)

#line below is equivolent to the commented line above, using **kwargs
sshClient.connect(**r1, look_for_keys=False, allow_agent=False)

print(sshClient.get_transport().is_active())

print('Closing Connection')
sshClient.close()