import React from "react";
import styles from "./OrganizerCard.module.css";
import { Link } from "react-router-dom";

export default function OrganizerCard({ item: organizer }) {
    return (
        <Link to={`/admin/organizers/${organizer.id}`} className={styles.card}>
            <div className={styles.image}>
                <img src={organizer.logo} alt={organizer.name} />                
            </div>
            <h2>{organizer.name}</h2>
        </Link>
    );
}
