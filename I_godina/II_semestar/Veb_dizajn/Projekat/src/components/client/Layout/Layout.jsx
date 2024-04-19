import React, {useEffect} from 'react';
import { Outlet } from 'react-router-dom';
import Navbar from '../Navbar/Navbar';
import Footer from '../Footer/Footer';

const Layout = () => {
    
    useEffect(() => {
        document.body.style.backgroundColor = `var(--color-bg-main)`;
    }, []);
    return (
        <>
            <Navbar />
            <main style={{flex: 1}}>
                <Outlet />
            </main>
            <Footer />
        </>
    );
};

export default Layout;