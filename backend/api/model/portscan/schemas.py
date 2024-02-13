from pydantic import BaseModel, Field

class PortScanBase(BaseModel):
    ip: str = Field(...)

class PortScan(PortScanBase):
    ip : str
