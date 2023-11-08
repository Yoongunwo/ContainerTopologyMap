import React from 'react';
import { createBrowserRouter } from 'react-router-dom';

import Home from '../pages/Home/home';
import Topology from '../pages/containerTopology/Topology';
import MainLayout from '../layout/MainLayout';
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
        ],
    },
]);
export default Router;
