from fastapi import APIRouter, Depends, HTTPException, Query, Response

import paramiko
from model.ssh import schemas as ssh_shemas
from service import sshConnection

import api.sshconn as sshconn

from service import topologyNodes

router = APIRouter (
    prefix='/nodes',
    tags=['nodes'],
    responses={404: {'description': 'Not found'}},
)

@router.get('/getTotalNodes')
async def getTotalNodes():
    print('hi', sshconn.ssh_connection)
    masterNode = topologyNodes.getNodes(sshconn.ssh_connection)

    return masterNode
