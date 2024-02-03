import paramiko

from model.ssh import schemas as ssh_shemas

def sshConnection(sshInfo : ssh_shemas.SshConnection):
    ssh_connection = paramiko.SSHClient()
    
    ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # SSH 연결
    # ssh_connection.connect(hostname=sshInfo.ip, port=int(sshInfo.port), 
    #                    username=sshInfo.userName, password=sshInfo.password)
    
    ssh_connection.connect(hostname=sshInfo.ip, username=sshInfo.userName, password=sshInfo.password)

    return ssh_connection


