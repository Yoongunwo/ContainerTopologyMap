import AppConfig from '../core/config';

const fetchSshConnectionCreate = async (sshInfo) => {
    const url = `${AppConfig.api_base_url}/sshconn/create`;
    console.log('hi', sshInfo);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(sshInfo),
    });
    return response;
};

const fetchNodeList = async () => {
    const url = `${AppConfig.api_base_url}/nodes/getTotalNodes`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
    });
    return response;
};

export { fetchSshConnectionCreate, fetchNodeList };
