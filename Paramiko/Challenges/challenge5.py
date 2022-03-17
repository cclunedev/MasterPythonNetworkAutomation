#Script that connects to a Cisco Router using SSH and Paramiko. The script should enter enable mode, execute the show running-config command.
#Output of the command should be saved to a text file in the current directory

import paramiko, time, getpass

#Router SSH Connection Initialization
sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())


routerPassword = getpass.getpass('Enter r1 password:')
enablePass = getpass.getpass('Enter r1 enable password:')
r1 = {'hostname': '192.168.122.10', 'port':'22', 'username': 'admin', 'password': routerPassword}

print(f'Connecting to {r1["hostname"]}')
sshClient.connect(**r1, look_for_keys=False, allow_agent=False)
shell = sshClient.invoke_shell()

#Start Cisco Device Commands
shell.send('terminal length 0\n')
shell.send('enable\n')
shell.send(enablePass + '\n')
shell.send('show run \n')
time.sleep(1)
#End Cisco Device Commands

#Print the Cisco device CLI Output
output = shell.recv(10000)
output = output.decode('utf-8')

outputList = output.splitlines()
outputList = outputList[11:-1]
outputText = '\n'.join(outputList)

with open('Paramiko/Challenges/r1RunningConfig.txt','w') as file:
  file.write(outputText)

#Close SSH connection if it's active
if sshClient.get_transport().is_active() == True:
  print('Closing Connection')
  sshClient.close()