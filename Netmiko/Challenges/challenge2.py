#Python script that connects to a Cisco Router using SSH and Netmiko. The script should execute the show arp command in order to display the ARP table.
from netmiko import ConnectHandler

with open('challenge2DeviceInfo.txt', 'r') as file:
  deviceInfo = file.read().split(':')

cisco_device = {
  'device_type': 'cisco_ios',
  'host': deviceInfo[0],
  'username': deviceInfo[2],
  'password': deviceInfo[3],
  'port': deviceInfo[1],
  'secret': deviceInfo[4],
  'verbose': True
}


connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()

print('Entering enable mode...')
connection.enable()

output = connection.send_command('show arp')
print(output)



print('Closing connection')
connection.disconnect()