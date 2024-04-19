import React, { useEffect, useState } from "react";
import { useAppContext } from "../../../context/contextProvider";
import styles from "./Login.module.css";
import toast from "react-hot-toast";
import {IoEyeOutline} from "@react-icons/all-files/io5/IoEyeOutline";
import {IoEyeOffOutline} from "@react-icons/all-files/io5/IoEyeOffOutline";

export default function Login() {
    const {modal, data, setUser} = useAppContext()
    const [showPassword, setShowPassword] = useState(false)
    const [allowSubmit, setAllowSubmit] = useState(true)

    async function handleSubmit(event) {
        event.preventDefault();
        if(!allowSubmit) return;
        setAllowSubmit(false);
        const username = event.target.username.value;
        const password = event.target.password.value;
        if(!username) {
            toast.error("Please enter a username.");
            setAllowSubmit(true);
            return;
        } 
        if(!password) {
            toast.error("Please enter a password.");
            setAllowSubmit(true);
            return;
        } 
        for(const user of data.users) {
            if(user.username === username && user.password === password) {
                setUser(user);
                modal.close();
                toast.success(`Successfully logged in as ${user.name} ${user.surname}!\n Welcome back!`);
                setAllowSubmit(true);
                return;
            }
        }
        toast.error("Invalid username or password.\n Please try again.");
        setAllowSubmit(true);
    }

    return (
        <form className={styles.form} onSubmit={handleSubmit}>
            <h1>Login</h1>
            <div className={styles.inputs}>
                <div>
                    <label htmlFor="username">Username:</label>
                    <input type="text" id="username" />
                </div>
                <div className={styles.pass}>
                    <label htmlFor="password">Password:</label>
                    <input  type={showPassword ? "text" : "password"} id="password" />
                    <button type="button" onClick={() => setShowPassword(!showPassword)}>
                        {showPassword ? <IoEyeOffOutline size={20} /> : <IoEyeOutline size={20} />}
                    </button>
                </div>
            </div>
            <div className={styles.buttons}>
                <button type="submit">Login</button>
                <button type="button" onClick={modal.close}>Cancel</button>
            </div>
        </form>
    );
}

export const loginWrapperClassName = styles.wrapper;