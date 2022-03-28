import myparamikochallange as myparamiko
import threading


def execute_file_commands(router):
  ssh_client = myparamiko.connect(router['server_ip'], router['server_port'], router['user'], router['passwd'])
  shell = myparamiko.get_shell(ssh_client)

  myparamiko.send_from_file(shell, router['config'])

  print(myparamiko.show(shell))
  myparamiko.close(ssh_client)

router1 = {'server_ip': '192.168.122.10', 'server_port': '22', 'user':'admin', 'passwd':'cisco', 'config':'ospf.txt'}
router2 = {'server_ip': '192.168.122.20', 'server_port': '22', 'user': 'admin', 'passwd': 'cisco', 'config':'eigrp.txt'}
router3 = {'server_ip': '192.168.122.30', 'server_port': '22', 'user': 'admin', 'passwd': 'cisco', 'config':'router3.conf'}



routers = [router1, router2, router3]
threads = list()
for router in routers:
  th = threading.Thread(target=execute_file_commands, args=(router,))
  threads.append(th)
    
for th in threads:
  th.start()
    
for th in threads:
  th.join()