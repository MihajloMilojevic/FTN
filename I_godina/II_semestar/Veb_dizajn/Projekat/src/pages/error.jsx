import React from 'react';
import { Link, useParams, useSearchParams } from 'react-router-dom';
import useTitle from "../hooks/useTitle";
import styles from "../styles/error.module.css"

const ErrorPage = ({url}) => {
    const [params] = useSearchParams();
    useTitle(`Error ${params.get("code") ?? 500} | FestiPlan`)
    return (
        <div className={styles.page}>
            <h1>Error {params.get("code") ?? 500}</h1>
            <p>{params.get("msg") ?? "There was on error. Please try again later."}</p>
            <Link to={url}>Go back to the homepage</Link>
        </div>
    );
};

export default ErrorPage;