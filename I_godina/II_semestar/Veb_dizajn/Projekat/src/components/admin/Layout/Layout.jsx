import React, { useEffect } from 'react';
import { Outlet } from 'react-router-dom';
import Navbar from '../Navbar/Navbar';
import Footer from '../Footer/Footer';
import Tabs from '../Tabs/Tabs';
import styles from './Layout.module.css';

const Layout = () => {

    useEffect(() => {
        document.body.style.backgroundColor = `var(--color-bg-secondary)`;
    }, []);

    return (
        <>
            <Navbar />
            <Tabs />
            <main className={styles.main}>
                <div className={styles.wrapper}>
                    <div className={styles.content}>
                        <Outlet />
                    </div>
                </div>
            </main>
            <Footer />
        </>
    );
};

export default Layout;