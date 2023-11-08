import React from 'react';
import { Outlet } from 'react-router-dom';

import Header from '../components/Header';

const MainLayout = () => {
    return (
        <div>
            <Header />
            <div className="flex w-full h-full min-h-screen p-5">
                <Outlet />
            </div>
        </div>
    );
};
export default MainLayout;
