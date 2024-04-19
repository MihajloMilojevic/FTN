import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Footer.module.css';
import { SearchableText } from '../../common';

function Footer() {
    return (
        <footer className={styles.footer}>
            <div className={styles.logo}>
                {/* <Link to="/"> */}
                    <img src="/Logo.svg" alt="Logo" />
                {/* </Link> */}
            </div>
            <ul className={styles.list}>
                <li className={`${styles.link}`}><SearchableText text="Login" /></li>
                <li className={`${styles.link}`}><SearchableText text="Register" /></li>
                <li className={`${styles.link}`}><Link to="/admin"><SearchableText text="Admin" /></Link> </li>
            </ul>
            <div className={styles.contact}>
                <p className={styles.link}><a href="mailto:milojevicm374@gmail.com"><SearchableText text="milojevicm374@gmail.com" /></a></p>
                <p className={styles.link}><a href="tel:+381649781191"><SearchableText text="+381 64 97 811 91" /></a></p>
            </div>
        </footer>
    );
};

export default Footer;