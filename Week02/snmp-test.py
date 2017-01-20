from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP = '184.105.247.70'

a_device = (IP, COMMUNITY_STRING, SNMP_PORT)
OID = '1.3.6.1.2.1.1.1.0'

snmp_data = snmp_get_oid(a_device, oid=OID)
output = snmp_extract(snmp_data)
print output
