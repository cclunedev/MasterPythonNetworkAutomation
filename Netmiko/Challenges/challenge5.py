#Python script that connects to a Cisco Router using SSH and Netmiko. The script should execute the show ip int brief and show run commands and save the output as a file.
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
prompt = connection.find_prompt()
hostname = prompt[0:-1]

print('Entering enable mode...')
connection.enable()


output = connection.send_command('show ip int brief')
with open(f'Netmiko/Challenges/challenge5Output/{hostname}_show_ip_int_brief.txt', 'w') as file:
  file.write(output)

output = connection.send_command('show run')
with open(f'Netmiko/Challenges/challenge5Output/{hostname}_running_config.txt', 'w') as file:
  file.write(output)





print('Closing connection')
connection.disconnect()