import paramiko
import time

def disable_paging(remote_conn,command="terminal length 0\n", delay=1):
    remote_conn.send("\n")
    remote_conn.send(command)

    #Wait for complete
    time.sleep(delay)

    output = remote_conn.recv(65535)

    return output

if __name__ == "__main__":

    ip = '184.105.247.70'
    username = 'admin'
    password = 'dikstra'

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip, username=username, password=password)
    remote_conn = remote_conn_pre.invoke_shell()

    output = remote_conn.recv(5000)
    output = disable_paging(remote_conn)

    remote_conn.send("\n")
    remote_conn.send("show version\n")

    # Wait
    time.sleep(1)

    output = remote_conn.recv(65535)
    print output
    remote_conn_pre.close()
