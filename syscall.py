import paramiko
import time
import re
import json

# SSH 클라이언트 객체 생성
ssh_client = paramiko.SSHClient()

# 호스트 키 자동 추가 설정 (옵션)
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# SSH 연결
ssh_client.connect(hostname='192.168.1.10', username='root', password='vagrant')

# 원격 명령 실행
stdin, stdout, stderr = ssh_client.exec_command('kubectl get nodes -o wide')  # 예: 원하는 명령어 입력
nodesInfo = stdout.read().decode('utf-8')
nodesInfo = nodesInfo.split('\n')
nodesInfo = nodesInfo[1:-1]
nodesInfo = [re.split(r'\s{2,}', node) for node in nodesInfo]
nodesInfo = [{'name': node[0], 'status': node[1], 'roles': node[2], 'age': node[3],
            'kubernetes version': node[4], 'ip': node[5], 'os-image': node[7], 'kind':'node',
            'children':[{'name': 'pod', 'children': []}]} for node in nodesInfo]

stdin, stdout, stderr = ssh_client.exec_command('kubectl get pods --all-namespaces -o wide')  # 예: 원하는 명령어 입력
podsInfo = stdout.read().decode('utf-8')
print(podsInfo)
podsInfo = podsInfo.split('\n')
podsInfo = podsInfo[1:-1]
podsInfo = [re.split(r'\s{2,}', pod) for pod in podsInfo]
podsInfo = [{'namespace': pod[0], 'name': pod[1], 'ready': pod[2], 
             'status': pod[3], 'restarts': pod[4], 'age': pod[5],
             'ip': pod[6], 'node':pod[7], 'kind': 'pod'} for pod in podsInfo]


for pod in podsInfo:
    for node in nodesInfo:
        if pod['node'] == node['name']:
            node['children'][0]['childen'].append(pod)

nodes = {'name': 'node', 'children': []}
for node in nodesInfo:
    if node['roles'] == 'master':
        masterNode = node
    else:
        nodes['children'].append(node)

masterNode['children'].append(nodes)

print(json.dumps(masterNode, ensure_ascii=False, indent=3)) 

ssh_client.close()