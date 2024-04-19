import React from 'react';
import { Link } from 'react-router-dom';
import useTitle from "../hooks/useTitle";
import styles from "../styles/error.module.css"

const Error404 = ({url}) => {
    useTitle("404 Page Not Found | FestiPlan")
    return (
        <div className={styles.page}>
            <h1>404 Page Not Found</h1>
            <p>Oops! The page you are looking for does not exist.</p>
            <Link to={url}>Go back to the homepage</Link>
        </div>
    );
};

export default Error404;
