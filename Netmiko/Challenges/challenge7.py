#Python script that connects to a Cisco Router using SSH and Netmiko. The script should create a user and then save the running configuration of the router.
from netmiko import ConnectHandler


username = input('Enter New User Username:')
password = input('Enter New User Enable Password:')

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
prompt = connection.find_prompt()
hostname = prompt[0:-1]

print('Entering enable mode...')
connection.enable()

connection.send_command(f'username {username} secret {password}')
connection.send_command('write')





print('Closing connection')
connection.disconnect()