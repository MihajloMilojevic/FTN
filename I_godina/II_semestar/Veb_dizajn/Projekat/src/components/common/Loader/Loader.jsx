import React, { useEffect } from 'react';
import styles from './Loader.module.css';


const Loader = ({ isLoading,}) => {
    useEffect(() => {
        if (isLoading) {
            document.body.style.overflowY = 'hidden';
        } else {
            document.body.style.overflowY = 'auto';
        }
    }, [isLoading]);
    return (
        <div className={`${styles.overlay} ${isLoading ? styles.visible : ""}`}>
            <img src="/loader.svg" alt="Loader" />
        </div>
    );
};

export default Loader;