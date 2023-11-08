from pydantic import BaseModel, Field

class SshBase(BaseModel):
    userName: str = Field(...)
    password: str = Field(...)
    ip: str = Field(...)
    port: str = Field(...)

class SshConnection(SshBase):
    pass

class Ssh(SshBase):
    userName : str
    password : str
    ip : str
    port : str