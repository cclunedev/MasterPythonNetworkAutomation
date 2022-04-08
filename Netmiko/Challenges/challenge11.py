#Python script that connects to multiple Cisco Routers using SSH and Netmiko. The script should execute the show ip int brief command and display the output.
from netmiko import ConnectHandler

devices = []

for ip in ['192.168.122.10', '192.168.122.20', '192.168.122.30']:
  cisco_device = {
    'device_type': 'cisco_ios',
    'host': ip,
    'username': 'admin',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
  }
  devices.append(cisco_device)

deviceIPs = []

for device in devices:

  connection = ConnectHandler(**device)

  print('Entering enable mode...')
  connection.enable()

  output = connection.send_command('show ip int brief')
  print(output)


  print('#'*30)


  print('Closing connection')
  connection.disconnect()