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





print('Closing connection')
connection.disconnect()