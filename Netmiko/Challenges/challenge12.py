#Python script that connects to multiple Cisco Routers using SSH and Netmiko. The script should execute the show ip int brief command and display the output.
from sqlite3 import connect
from netmiko import ConnectHandler
from datetime import date

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
today = date.today()
print(today)


for device in devices:

  connection = ConnectHandler(**device)
  prompt = connection.find_prompt()[0:-1]
  print('Entering enable mode...')
  connection.enable()

  output = connection.send_command('show ip int brief')
  
  with open(f'Netmiko/Challenges/challenge12Output/{prompt}-{today}-ip-brief.txt','w') as file:
    file.write(output)


  print('Closing connection')
  connection.disconnect()