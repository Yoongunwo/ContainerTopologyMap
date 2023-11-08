import paramiko
import re

from model.ssh import schemas as ssh_shemas

def getNodes(ssh_client : paramiko.SSHClient):
    print(ssh_client)
    stdin, stdout, stderr = ssh_client.exec_command('kubectl get nodes -o wide')  # 예: 원하는 명령어 입력

# 결과 출력
    nodesInfo = stdout.read().decode('utf-8')

# nodesInfo to json 
    nodesInfo = nodesInfo.split('\n')
    nodesInfo = nodesInfo[1:-1]
    nodesInfo = [re.split(r'\s{2,}', node) for node in nodesInfo]
    nodesInfo = [{'name': node[0], 'ip': node[5], 'status': node[1], 'roles': node[2], 'os-image': node[7]} for node in nodesInfo]

# if nodesInfo[i].roles != 'master': all nodes place under the master node to json, key is childern 
    childern = []
    masterNode = {}
    for node in nodesInfo:
        if node['roles'] == 'master':
            masterNode = node
        else:
            childern.append(node)

    masterNode['children'] = childern
    print(masterNode)
    return masterNode