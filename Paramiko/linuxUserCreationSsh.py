import myparamiko
import getpass

username = input("Enter A Linux Root Username:")
password = getpass.getpass()
linuxServer = {'server_ip': '127.0.0.1', 'server_port': '22', 'user': username, 'passwd': password }

addUser = input('Enter username of new Linux user:')

print('sudo useradd -m -d /home/' + addUser + ' -s /bin/bash ' + addUser)

if input('Enter Y to view user list:') == 'Y':
  displayUsers = True
else:
  displayUsers = False

client = myparamiko.connect(**linuxServer)
shell = myparamiko.get_shell(client)
myparamiko.send_command(shell, 'sudo useradd -m -d /home/' + addUser + ' -s /bin/bash ' + addUser)
myparamiko.send_command(shell, password)

if displayUsers:
  users = myparamiko.send_command(shell, 'cat /etc/passwd').decode()
  print(users)

myparamiko.close(client)