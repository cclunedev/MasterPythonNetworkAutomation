#Script that connects to a Cisco Router using SSH and Paramiko and executes all the commands from a text file.
#Commands are stored per line

#Script that connects to a Cisco Router using SSH and Paramiko and executes a list of commands. The commands are saved in a Python list.

import paramiko, time, getpass

#Process Command Text File
with open('Paramiko/Challenges/commands.txt', 'r') as commandsFile:
  commandsList = commandsFile.readlines()
  print(commandsList)

#Router SSH Connection Initialization
sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

routerPassword = getpass.getpass('Enter r1 password:')
r1 = {'hostname': '192.168.122.10', 'port':'22', 'username': 'admin', 'password': routerPassword}

print(f'Connecting to {r1["hostname"]}')
sshClient.connect(**r1, look_for_keys=False, allow_agent=False)
shell = sshClient.invoke_shell()

#Start Cisco Device Commands
for command in commandsList:
  shell.send(command)
time.sleep(3)
#End Cisco Device Commands

#Print the Cisco device CLI Output
output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

#Close SSH connection if it's active
if sshClient.get_transport().is_active() == True:
  print('Closing Connection')
  sshClient.close()