#Python script that connects to a Cisco Router using SSH and Netmiko. The script should get the prompt, process it and then print the hostname part.
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
print(hostname)






print('Closing connection')
connection.disconnect()