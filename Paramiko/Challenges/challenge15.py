import paramiko
import time
import threading

def execute_command(router, command):
  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  print(f'Connecting to {router["hostname"]}')
  ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
  
  shell = ssh_client.invoke_shell()
  
  print(f'Sending command: {command}')
  shell.send('term length 0\n')
  shell.send(command + '\n')
  time.sleep(1)

  output = shell.recv(100000)
  print(output.decode())

  if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()

if __name__ == '__main__':
    router1 = {'hostname': '192.168.122.10', 'port': '22', 'username':'admin', 'password':'cisco'}
    router2 = {'hostname': '192.168.122.20', 'port': '22', 'username':'admin', 'password':'cisco'}
    router3 = {'hostname': '192.168.122.30', 'port': '22', 'username':'admin', 'password':'cisco'}

    routers = [router1, router2, router3]
    threads = list()
    for router in routers:
      th = threading.Thread(target=execute_command, args=(router, 'show ip interface brief'))
      threads.append(th)
    
    for th in threads:
      th.start()
    
    for th in threads:
      th.join()