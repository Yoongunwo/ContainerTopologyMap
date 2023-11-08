import paramiko
import time
import re

# SSH 클라이언트 객체 생성
ssh_client = paramiko.SSHClient()

# 호스트 키 자동 추가 설정 (옵션)
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# SSH 연결
ssh_client.connect(hostname='192.168.1.10', port=22, username='root', password='glove2274')

# 원격 명령 실행
stdin, stdout, stderr = ssh_client.exec_command('kubectl get nodes -o wide')  # 예: 원하는 명령어 입력

# 결과 출력
nodesInfo = stdout.read().decode('utf-8')
#print(nodesInfo)

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
print(ssh_client)

# stdin, stdout, stderr = ssh_client.exec_command('sysdig')
# time.sleep(5)
# stdin, stdout, stderr = ssh_client.exec_command('^C')
# print(stdout.read().decode('utf-8'))
ssh_client.close()