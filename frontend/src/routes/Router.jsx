import React from 'react';
import { createBrowserRouter } from 'react-router-dom';

import Home from '../pages/Home/home';
import Topology from '../pages/containerTopology/Topology';
import MainLayout from '../layout/MainLayout';
import PortScan from '../pages/portScan/portScan';

const Router = createBrowserRouter([
    {
        path: '/',
        element: <MainLayout />,
        children: [
            {
                index: true,
                element: <Home />,
            },
            {
                path: 'topology',
                element: <Topology />,
            },
            {
                path: 'portscan',
                element: <PortScan />,
            },
        ],
    },
]);
export default Router;
