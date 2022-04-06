#Python script that connects to a Cisco Router using SSH and Netmiko. The script should create an ACL (access control list) by executing 3 commands
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

commands = ['access-list 101 permit tcp any any eq 80',
            'access-list 101 permit tcp any any eq 443',
            'access-list 101 deny ip any any']


connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()
hostname = prompt[0:-1]

print('Entering enable mode...')
connection.enable()

output = connection.send_config_set(commands)
print(output)



print('Closing connection')
connection.disconnect()