import AppConfig from '../core/config';

const fetchPortScan = async (ipInfo) => {
    const url = `${AppConfig.api_base_url}/portscan/get`;
    console.log('hi', ipInfo);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(ipInfo),
    });
    console.log(response);
    return response;
};

export { fetchPortScan };
