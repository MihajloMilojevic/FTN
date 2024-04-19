import React from "react";
import { NavLink } from "react-router-dom";
import styles from "./Tabs.module.css";

export default function Tabs() {
    return (
        <div className={styles.tabs}>
            <NavLink className={({isActive}) => `${styles.tab} ${isActive ? styles.active : ""}`} to="/admin/organizers">Organizers</NavLink>
            <NavLink className={({isActive}) => `${styles.tab} ${isActive ? styles.active : ""}`} to="/admin/users">Users</NavLink>
        </div>
    );
}