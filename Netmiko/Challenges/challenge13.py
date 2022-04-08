#execute() that has 2 arguments: a device of type dictionary and a command to execute on that device. After executing the command the function will disconnect.
#The function will use Netmiko to connect and execute the command on the device.

def execute(deviceDict, commandString):
  from netmiko import ConnectHandler

  connection = ConnectHandler(**deviceDict)

  print('Entering enable mode...')
  connection.enable()
  output = connection.send_command(commandString)
  print(output)

  print('Closing connection')
  connection.disconnect()




if __name__ == '__main__':
  cisco_device = {
      'device_type': 'cisco_ios',
      'host': '192.168.122.10',
      'username': 'admin',
      'password': 'cisco',
      'port': 22,
      'secret': 'cisco',
      'verbose': True
    }
  command = 'show ip interface brief'

  execute(cisco_device, command)

