from netmiko import ConnectHandler
from datetime import datetime
from DEVICE_CREDS import all_devices

start_time = datetime.now()

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    device_name = net_connect.find_prompt()
    output = net_connect.send_command("show arp")
    print "\n\n>>>>>>>Device {0} <<<<<<<<".format(device_name)
    print output
    print ">>>>>>> End <<<<<<<"
    
end_time = datetime.now()
total_time = end_time - start_time
