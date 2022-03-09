import paramiko, time, getpass

sshClient = paramiko.SSHClient()
print(type(sshClient))
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())


routerPassword = getpass.getpass('Enter r1 password:')
r1 = {'hostname': '192.168.122.10', 'port':'22', 'username': 'admin', 'password': routerPassword}

print(f'Connecting to {r1["hostname"]}')
sshClient.connect(**r1, look_for_keys=False, allow_agent=False)
shell = sshClient.invoke_shell()

#Start Cisco Device Commands
shell.send('terminal length 0\n')
shell.send('enable\n')
shell.send('cisco\n')
shell.send('config t\n')

shell.send('router ospf 1\n')
shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
shell.send('do show ip ospf\n')
time.sleep(2)
#End Cisco Device Commands

#Print the Cisco device CLI Output
output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

#Close SSH connection if it's active
if sshClient.get_transport().is_active() == True:
  print('Closing Connection')
  sshClient.close()