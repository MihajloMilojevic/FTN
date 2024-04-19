import React, { useEffect } from 'react';
import styles from './Modal.module.css';


const Modal = ({ isOpen, children, useDefaultStyles, contentWrapperStyles, contentWrapperClassName }) => {
    useEffect(() => {
        if (isOpen) {
            document.body.style.overflowY = 'hidden';
        } else {
            document.body.style.overflowY = 'auto';
        }
    }, [isOpen]);
    return (
        <div className={`${styles.overlay} ${isOpen ? styles.visible : ""}`}>
            <div className={`${useDefaultStyles ? styles.content : ""} ${contentWrapperClassName}`} style={{...(contentWrapperStyles || {})}}>
                {children}
            </div>
        </div>
    );
};

export default Modal;