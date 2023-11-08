from fastapi import APIRouter, Depends, HTTPException, Query, Response

from model.ssh import schemas as ssh_shemas
from service import sshConnection

router = APIRouter (
    prefix='/sshconn',
    tags=['sshconn'],
    responses={404: {'description': 'Not found'}},
)

ssh_connection = None

@router.get('/create')
def hi():
    return {'message': 'hi'}

@router.post('/create')
async def createSshConnection(ssh : ssh_shemas.SshConnection):
    global ssh_connection
    ssh_connection = sshConnection.sshConnection(ssh)
    return {'message': 'success'}
