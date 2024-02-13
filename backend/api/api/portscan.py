from fastapi import APIRouter, Depends, HTTPException, Query, Response

from model.portscan import schemas as portscan_schemas

router = APIRouter (
    prefix='/portscan',
    tags=['portscan'],
    responses={404: {'description': 'Not found portscan'}},
)

@router.get('/get')
def hi():
    return {'message': 'hi'}

@router.post('/get')
async def portscan(portScan : portscan_schemas.PortScan):
    portscanResult = portScan
    print(portscanResult.ip)
    return {'message': 'hi'}