main_username = 'pyclass'
main_password = '88newclass'

arista_username = 'admin1'
arista_password = '99saturday'

cisco_rtr01 = {
'device_type': 'cisco_ios',
'ip':   '184.105.247.70',
'username': main_username,
'password': main_password,
'verbose': False,
}

cisco_rtr02 = {
'device_type': 'cisco_ios',
'ip':   '184.105.247.71',
'username': main_username,
'password': main_password,
'verbose': False,
}

arista_sw01 = {
'device_type': 'arista_eos',
'ip':   '184.105.247.72',
'username': arista_username,
'password': arista_password,
'verbose': False,
}

arista_sw02 = {
'device_type': 'arista_eos',
'ip':   '184.105.247.73',
'username': arista_username,
'password': arista_password,
'verbose': False,
}

arista_sw03 = {
'device_type': 'arista_eos',
'ip':   '184.105.247.74',
'username': arista_username,
'password': arista_password,
'verbose': False,
}

arista_sw04 = {
'device_type': 'arista_eos',
'ip':   '184.105.247.75',
'username': arista_username,
'password': arista_password,
'verbose': False,
}

juniper_srx01 = {
'device_type': 'juniper',
'ip':   '184.105.247.76',
'username': main_username,
'password': main_password,
'verbose': False,
}

all_devices = [cisco_rtr01,cisco_rtr02,arista_sw01,arista_sw02,arista_sw03,arista_sw04,juniper_srx01]
