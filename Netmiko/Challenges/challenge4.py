#Python script that connects to a Cisco Router using SSH and Netmiko. The script should execute the show ip int brief and show run commands.
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


connection = ConnectHandler(**cisco_device)

print('Entering enable mode...')
connection.enable()

output = connection.send_command('show ip int brief')
print(output)

print('#'*30)

output = connection.send_command('show run')
print(output)





print('Closing connection')
connection.disconnect()