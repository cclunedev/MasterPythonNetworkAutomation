def send_from_list(commandList): 
  #Function that connects to a Cisco Router using SSH and Paramiko and executes the argument list of commands.

  import paramiko, time, getpass

  #Router SSH Connection Initialization
  sshClient = paramiko.SSHClient()
  sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  routerPassword = getpass.getpass('Enter r1 password:')
  r1 = {'hostname': '192.168.122.10', 'port':'22', 'username': 'admin', 'password': routerPassword}

  print(f'Connecting to {r1["hostname"]}')
  sshClient.connect(**r1, look_for_keys=False, allow_agent=False)
  shell = sshClient.invoke_shell()

  #Start Cisco Device Commands
  for command in commandList:
    shell.send(command + '\n')
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

send_from_list(['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user'])