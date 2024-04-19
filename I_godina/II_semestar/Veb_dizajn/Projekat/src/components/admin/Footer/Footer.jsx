import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Footer.module.css';
import { SearchableText } from '../../common';
import { useAppContext } from '../../../context/contextProvider';
import APIs from '../../../api/API';
import toast from 'react-hot-toast';

function Footer() {
    const {modal, setData} = useAppContext();

    async function reset() {
        const {error, data} = await APIs.resetData();
        if(error) {
            toast.error("Failed to reset data");
            return
        }
        setData(data);
    }

    function handleReset() {
        modal.open(<ConfirmationModal onConfirm={reset} />);
    }

    return (
        <footer className={styles.footer}>
            <div className={styles.logo}>
                <Link to="/admin">
                    <img src="/Logo.svg" alt="Logo" />
                </Link>
            </div>
            <ul className={styles.list}>
                <li className={`${styles.link}`}><SearchableText text="Login" /></li>
                <li className={`${styles.link}`}><SearchableText text="Register" /></li>
                <li className={`${styles.link}`}><Link to="/"><SearchableText text="Client" /></Link> </li>
                <li className={`${styles.link}`}>
                    <button className={styles.reset_button} onClick={handleReset}>
                        Reset Data
                    </button>
                </li>
            </ul>
            <div className={styles.contact}>
                <p className={styles.link}><a href="mailto:milojevicm374@gmail.com"><SearchableText text="milojevicm374@gmail.com" /></a></p>
                <p className={styles.link}><a href="tel:+381649781191"><SearchableText text="+381 64 97 811 91" /></a></p>
            </div>
        </footer>
    );
};

export default Footer;

function ConfirmationModal({onConfirm}) {
    const {modal} = useAppContext();
    function handleConfirm() {
        modal.close();
        onConfirm();
    }
    function handleCancel() {
        modal.close();
    }
    return (
        <div>
            <h2>Are you sure you want to reset the data?</h2>
            <div className={styles.buttons} style={{marginTop: "0.75rem"}}>
                <div>
                    <button onClick={handleConfirm} className={styles.main}>Yes</button>
                    <button onClick={handleCancel}>No</button>
                </div>
            </div>
        </div>
    )
}