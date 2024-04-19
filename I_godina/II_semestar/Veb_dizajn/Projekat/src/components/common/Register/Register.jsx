import React, { useEffect, useState } from "react";
import { useAppContext } from "../../../context/contextProvider";
import styles from "./Register.module.css";
import toast from "react-hot-toast";
import {IoEyeOutline} from "@react-icons/all-files/io5/IoEyeOutline";
import {IoEyeOffOutline} from "@react-icons/all-files/io5/IoEyeOffOutline";
import { User } from "../../../models";
import APIs from "../../../api/API";

const initialFormData = {
    name: { value: "", error: null}, surname: { value: "", error: null}, email: { value: "", error: null}, username: { value: "", error: null}, password: { value: "", error: null}, confirm: { value: "", error: null}, address: { value: "", error: null}, profession: { value: "", error: null}, phone: { value: "", error: null}, birthday: { value: "", error: null }
};

export default function Register() {
    const {modal, data, setUser, setData} = useAppContext()
    const [showPassword, setShowPassword] = useState(false)
    const [showConfirm, setShowConfirm] = useState(false)
    const [allowSubmit, setAllowSubmit] = useState(false)
    const [currentStep, setCurrentStep] = useState(0)
    const [formData, setFormData] = useState(initialFormData)

    async function handleSubmit(event) {
        event.preventDefault();
        if(!allowSubmit) return;
        if(
            (formData.name.error || formData.surname.error || formData.email.error) || 
            (formData.name.error == null || formData.surname.error == null || formData.email.error == null) ||
            (formData.username.error || formData.password.error || formData.confirm.error) || 
            (formData.username.error == null || formData.password.error == null || formData.confirm.error == null) ||
            (formData.address.error || formData.profession.error || formData.phone.error || formData.birthday.error) || 
            (formData.address.error == null || formData.surname.error == null || formData.phone.error == null | formData.birthday.error == null)
        ) {
            toast.error("Please fill in all required fields.");
            return;
        }
        if(formData.password.value.length < 8) {
            toast.error("Please enter a password that is at least 8 characters long.");
            return;
        }
        else if(!/[A-Z]/.test(formData.password.value)) {
            toast.error("Password must include at least one uppercase character.");
            return;
        }
        else if(!/[a-z]/.test(formData.password.value)) {
            toast.error("Password must include at least one lowercase character.");
            return;
        }
        else if(!/[0-9]/.test(formData.password.value)) {
            toast.error("Password must include at least one digit.");
            return;
        }
        else if(formData.password.value.replace(/[A-Za-z0-9]/gi, "").length === 0) {
            toast.error("Password must include at least one special character.");
            return;
        }
        const newUser = new User("", formData.username.value, formData.password.value, formData.name.value, formData.surname.value, formData.email.value, formData.birthday.value, formData.address.value, formData.phone.value, formData.profession.value);
        const {data: createdData, error} = await APIs.createUser(newUser);
        if(error) {
            toast.error("Failed to register user.");
            return;
        }
        newUser.id = createdData.name;
        setUser(newUser);
        setData({...data, users: [...data.users, newUser]})
        toast.success(`Successfully registered as ${newUser.name} ${newUser.surname}!\n Welcome!`);
        modal.close();
    }

    function handleNext() {
        if(currentStep === 2) return;
        switch(currentStep) {
            case 0:
                if(
                    (formData.name.error || formData.surname.error || formData.email.error) || 
                    (formData.name.error == null || formData.surname.error == null || formData.email.error == null)
                ) {
                    toast.error("Please fill in all required fields.");
                    return;
                }
                break;
            case 1:
                if((formData.username.error || formData.password.error || formData.confirm.error) || 
                    (formData.username.error == null || formData.password.error == null || formData.confirm.error == null)
                ) {
                    toast.error("Please fill in all required fields.");
                    return;
                }
                if(formData.password.value !== formData.confirm.value) {
                    toast.error("Passwords do not match.");
                    return;
                }    
                setAllowSubmit(true);
                break;
        }
        setCurrentStep(currentStep + 1);
    }
    function handlePrevious() {
        if(currentStep === 0) return;
        setAllowSubmit(false);
        setCurrentStep(currentStep - 1);
    }

    function handleOnlyRequiredChange(e) {
        const {name, value} = e.target;
        setFormData({...formData, [name]: {value, error: !value}});
    }

    function handleEmailChange(e) {
        const {name, value} = e.target;
        const emailRegex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
        setFormData({...formData, [name]: {value, error: !emailRegex.test(value)}});
    }
    function handlePasswordChange(e) {
        const {name, value} = e.target;
        let err = false;
        if(value.length < 8) err = true;
        else if(!/[A-Z]/.test(value)) err = true;
        else if(!/[a-z]/.test(value)) err = true;
        else if(!/[0-9]/.test(value)) err = true;
        else if(value.replace(/[A-Za-z0-9]/gi, "").length === 0) err = true;
        setFormData({...formData, [name]: {value, error: err}});
    }

    return (
        <form className={styles.form} onSubmit={handleSubmit}>
            <h1>Register {currentStep+1}/3</h1>
            <div style={{
                position: "relative",
                overflowX: "hidden",
                width: "100%",
                alignSelf: "stretch",
                flex: 1,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                flexDirection: "column"
            }}>
                <div className={styles.inputs} style={{
                    transform: `translateX(-${currentStep * 101}%)`
                }}>
                    <div>
                        <label htmlFor="name">Name:</label>
                        <input 
                            style={{
                                border: (formData.name.error != null ? 
                                    `2px solid ${(formData.name.error ? "red" : "green")}` : 
                                    "none")
                            }} 
                            type="text" id="name" name="name" 
                            value={formData.name.value} onChange={handleOnlyRequiredChange} 
                        />
                    </div>
                    <div>
                        <label htmlFor="surname">Surname:</label>
                        <input 
                            style={{
                                border: (formData.surname.error != null ? 
                                    `2px solid ${(formData.surname.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="text" id="surname" name="surname" 
                            value={formData.surname.value} onChange={handleOnlyRequiredChange} 
                        />
                    </div>
                    <div>
                        <label htmlFor="email">Email:</label>
                        <input 
                            style={{
                                border: (formData.email.error != null ? 
                                    `2px solid ${(formData.email.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="text" id="email" name="email" 
                            value={formData.email.value} onChange={handleEmailChange} 
                        />
                    </div>
                </div>
                <div className={styles.inputs} style={{
                    position: "absolute",
                    right: "-100%",
                    top: "50%",
                    transform: `translateX(calc(-${(currentStep) * 100}% ${currentStep === 2 ? "- 5px" : currentStep === 0 ? "+ 5px" : ""})) translateY(-50%)`
                }}>
                    <div>
                        <label htmlFor="username">Username:</label>
                        <input 
                            style={{
                                border: (formData.username.error != null ? 
                                    `2px solid ${(formData.username.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="text" id="username" name="username"
                            value={formData.username.value} onChange={handleOnlyRequiredChange}
                        />
                    </div>
                    <div className={styles.pass} title="Password must include at least one: lowercase character, uppercase character, digit and special character and must be at least 8 characters long!">
                        <label htmlFor="password">Password:</label>
                        <input 
                            style={{
                                border: (formData.password.error != null ? 
                                    `2px solid ${(formData.password.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type={showPassword ? "text" : "password"} id="password" name="password"
                            value={formData.password.value} onChange={handlePasswordChange}
                        />
                        <button type="button" onClick={() => setShowPassword(!showPassword)}>
                            {showPassword ? <IoEyeOffOutline size={20} /> : <IoEyeOutline size={20} />}
                        </button>
                    </div>
                    <div className={styles.pass} title="Password must include at least one: lowercase character, uppercase character, digit and special character and must be at least 8 characters long!">
                        <label htmlFor="confirm">Confirm password:</label>
                        <input 
                            style={{
                                border: (formData.confirm.error != null ? 
                                    `2px solid ${(formData.confirm.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type={showConfirm ? "text" : "password"} id="confirm" name="confirm"
                            value={formData.confirm.value} onChange={handlePasswordChange}
                        />
                        <button type="button" onClick={() => setShowConfirm(!showConfirm)}>
                            {showConfirm ? <IoEyeOffOutline size={20} /> : <IoEyeOutline size={20} />}
                        </button>
                    </div>
                </div>
                <div className={styles.inputs} style={{
                    transform: `translateX(-${(currentStep) * 100}%) translateY(-50%)`,
                    position: "absolute",
                    right: "-200%",
                    top: "50%"
                }}>
                    <div>
                        <label htmlFor="address">Address:</label>
                        <input 
                            style={{
                                border: (formData.address.error != null ? 
                                    `2px solid ${(formData.address.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="text" id="address" name="address"
                            value={formData.address.value} onChange={handleOnlyRequiredChange}
                        />
                    </div>
                    <div>
                        <label htmlFor="profession">Profession:</label>
                        <input 
                            style={{
                                border: (formData.profession.error != null ? 
                                    `2px solid ${(formData.profession.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="text" id="profession" name="profession"
                            value={formData.profession.value} onChange={handleOnlyRequiredChange}
                        />
                    </div>
                    <div>
                        <label htmlFor="phone">Phone:</label>
                        <input 
                            style={{
                                border: (formData.phone.error != null ? 
                                    `2px solid ${(formData.phone.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="tel" id="phone" name="phone" 
                            value={formData.phone.value} onChange={handleOnlyRequiredChange}
                        />
                    </div>
                    <div>
                        <label htmlFor="birthday">Date of birth:</label>
                        <input 
                            style={{
                                border: (formData.birthday.error != null ? 
                                    `2px solid ${(formData.birthday.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="date" id="birthday" name="birthday"
                            value={formData.birthday.value} onChange={handleOnlyRequiredChange}
                        />
                    </div>
                </div>
            </div>
            <div className={styles.buttons}>
                <div>
                    <button type="button" onClick={modal.close}>Cancel</button>
                    {currentStep === 2 && <button type="submit">Register</button>}
                </div>
                <div>
                    {
                        currentStep > 0 && <button type="button" onClick={handlePrevious}>Back</button>
                    }
                    {
                        currentStep < 2 && <button type="button" onClick={handleNext}>Next</button>
                    }
                </div>
            </div>
        </form>
    );
}

export const registerWrapperClassName = styles.wrapper;