import paramiko
import re
import json

from model.ssh import schemas as ssh_shemas

def getNodes(ssh_client : paramiko.SSHClient):
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
    podsInfo = podsInfo.split('\n')
    podsInfo = podsInfo[1:-1]
    podsInfo = [re.split(r'\s{2,}', pod) for pod in podsInfo]
    podsInfo = [{'namespace': pod[0], 'name': pod[1], 'ready': pod[2], 
                'status': pod[3], 'restarts': pod[4], 'age': pod[5],
                'ip': pod[6], 'node':pod[7], 'kind': 'pod'} for pod in podsInfo]  


    for pod in podsInfo:
        for node in nodesInfo:
            if pod['node'] == node['name']:
                node['children'][0]['children'].append(pod)

    nodes = {'name': 'node', 'children': []}
    for node in nodesInfo:
        if node['roles'] == 'master':
            masterNode = node
        else:
            nodes['children'].append(node)

    masterNode['children'].append(nodes)
    print(masterNode)
    return masterNode

def getPods(ssh_client : paramiko.SSHClient):
    stdin, stdout, stderr = ssh_client.exec_command('kubectl get pods --all-namespaces -o wide')  # 예: 원하는 명령어 입력
    podsInfo = stdout.read().decode('utf-8')
    podsInfo = podsInfo.split('\n')
    podsInfo = podsInfo[1:-1]
    podsInfo = [re.split(r'\s{2,}', pod) for pod in podsInfo]
    podsInfo = [{'namespace': pod[0], 'name': pod[1], 'ready': pod[2], 'status': pod[3], 'ip': pod[6], 'node':pod[7]} for pod in podsInfo]

    return podsInfo
 

def combineNodePod(nodes, pods):
    for pod in pods:
        if pod['node'] == nodes['name']:
            nodes['pods'].append(pod)
        else :
            for node in nodes['children']:
                if pod['node'] == node['name']:
                    node['pods'].append(pod)

    print(json.dumps(nodes, ensure_ascii=False, indent=3))    
    return nodes