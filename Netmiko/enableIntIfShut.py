from operator import contains
from netmiko import ConnectHandler

cisco_device = {
  'device_type': 'cisco_ios',
  'host': '192.168.122.10',
  'username': 'admin',
  'password': 'cisco',
  'port': 22,
  'secret': 'cisco',
  'verbose': True
}

interfaceToCheck = input('Enter full name of interface to enable:')

connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()

print('Entering enable mode...')
connection.enable()
output = connection.send_command(f'show ip interface {interfaceToCheck}')

if 'Invalid input detected' in output:
  print('You entered an invalid interface')

else:
  outputList = output.split()


  if 'administratively' in outputList:
    if not connection.check_config_mode():
      connection.config_mode()
    commands = [f'interface {interfaceToCheck}', 'no shut']
    connection.send_config_set(commands)
    connection.exit_config_mode()
    print(connection.send_command(f'show ip int brief | include {interfaceToCheck}'))
    print(f'{interfaceToCheck} was shutdown and has been no shut')

  elif 'up' in outputList:
    print('Interface is already up')
  else:
    print('Selected interface name not on device')

print('Closing connection')
connection.disconnect()