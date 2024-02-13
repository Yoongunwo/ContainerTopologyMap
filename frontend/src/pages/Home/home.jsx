import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';

import { Button, TextField } from '@mui/material';
import { fetchSshConnectionCreate } from '../../services/sshService';
import { fetchPortScan } from '../../services/portScanService';

const home = () => {
    const navigate = useNavigate();

    const [ip, setIp] = useState('');
    const [port, setPort] = useState('');
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [portScanIp, setPortScanIp] = useState('');

    const startTopology = () => {
        const sshConnection = {
            ip: ip,
            port: port,
            userName: userName,
            password: password,
        };
        console.log(sshConnection);
        fetchSshConnectionCreate(sshConnection).then(async (response) => {
            if (response.status === 200) {
                navigate('/topology');
            }
        });
    };
    const startPortScan = () => {
        const portScanInfo = {
            ip: portScanIp,
        };
        fetchPortScan(portScanInfo).then(async (response) => {
            if (response.status === 200) {
                navigate('/portscan');
            }
        });
    };
    return (
        <div className="flex w-full flex-col">
            <div className="flex w-full mb-5">
                <TextField
                    className="flex "
                    required
                    id="ip"
                    label="IP Address"
                    value={ip}
                    onChange={(e) => {
                        setIp(e.target.value);
                    }}
                />
            </div>
            <div className="flex w-full mb-5">
                <TextField
                    required
                    id="port"
                    label="Port Number"
                    value={port}
                    onChange={(e) => {
                        setPort(e.target.value);
                    }}
                />
            </div>
            <div className="flex w-full mb-5">
                <TextField
                    required
                    id="username"
                    label="SSH Username"
                    value={userName}
                    onChange={(e) => {
                        setUserName(e.target.value);
                    }}
                />
            </div>
            <div className="flex w-full mb-5">
                <TextField
                    required
                    id="password"
                    label="SSH password"
                    value={password}
                    onChange={(e) => {
                        setPassword(e.target.value);
                    }}
                />
            </div>
            <div>
                <Button variant="contained" onClick={startTopology}>
                    Topology
                </Button>
            </div>
            <div className="flex w-full mb-5">
                <p>Port Scan</p>
            </div>
            <div className="flex w-full mb-5">
                <TextField
                    required
                    id="portScanIp"
                    label="IP"
                    value={portScanIp}
                    onChange={(e) => {
                        setPortScanIp(e.target.value);
                    }}
                />
            </div>
            <div>
                <Button variant="contained" onClick={startPortScan}>
                    Port Scan
                </Button>
            </div>
        </div>
    );
};
export default home;
