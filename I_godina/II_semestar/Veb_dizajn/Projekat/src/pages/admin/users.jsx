import React, { useState } from 'react';
import useTitle from "../../hooks/useTitle";
import styles from "../../styles/admin/users.module.css"
import { useAppContext } from '../../context/contextProvider';
import {GiTrashCan} from "@react-icons/all-files/gi/GiTrashCan"
import {GiPencil} from "@react-icons/all-files/gi/GiPencil"
import toast from "react-hot-toast";
import { User } from "../../models";
import { SearchableText } from '../../components/common';
import APIs from '../../api/API';

function UsersPage() {
    useTitle(`Users | FestiPlan`)
    const {data, setData, modal} = useAppContext();

    async function deleteUser(user) {
        const deleted = await APIs.deleteUser(user.id);
        if (!deleted) {
            toast.error("Failed to delete user.");
            return;
        }
        toast.success("User deleted successfully.");
        setData({...data, users: data.users.filter(u => u.id !== user.id)})
    }

    function handleDelete(user) {
        modal.open(
            <ConfirmDeleteModal user={user} onConfirm={deleteUser} />
        )
    }

    async function editUser(newUser) {
        const updated = await APIs.updateUser(newUser);
        if (!updated) {
            toast.error("Failed to update user.");
            return;
        }
        toast.success("User updated successfully.");
        const copy = [...data.users];
        const index = copy.findIndex(u => u.id === newUser.id);
        copy[index] = newUser;
        setData({...data, users: copy});
    }

    function handleEdit(user) {
        modal.open(
            <EditUserModal user={user} onConfirm={editUser} />,
            {contentWrapperClassName: styles.wrapper    }
        )
    }

    return (
        <>
            <h1><SearchableText text="All registered users" /></h1>
            <div className={styles.table_wrapper}>
                <table className={styles.table}>
                    <thead>
                        <tr>
                            <th><SearchableText text="Username" /></th>
                            <th><SearchableText text="Name" /></th>
                            <th><SearchableText text="Surname" /></th>
                            <th><SearchableText text="Email" /></th>
                            <th><SearchableText text="Birthday" /></th>
                            <th><SearchableText text="Address" /></th>
                            <th><SearchableText text="Phone" /></th>
                            <th><SearchableText text="Profession" /></th>
                            <th colSpan={2}><SearchableText text="Actions" /></th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            data.users.map(user => {
                                const date = new Date(user.dateOfBirth);
                                return (
                                    <tr key={user.id}>
                                        <td><SearchableText text={user.username} /></td>
                                        <td><SearchableText text={user.name} /></td>
                                        <td><SearchableText text={user.surname} /></td>
                                        <td><SearchableText text={user.email} /></td>
                                        <td><SearchableText text={`${date.getDate()}.${date.getMonth()+1}.${date.getFullYear()}`} /></td>
                                        <td><SearchableText text={user.address} /></td>
                                        <td><SearchableText text={user.phone} /></td>
                                        <td><SearchableText text={user.profession} /></td>
                                        <td>
                                            <div className={styles.action_button} onClick={() => handleEdit(user)}>
                                                <GiPencil size={20} />
                                                <span>
                                                    <SearchableText text="Edit" />
                                                </span>
                                            </div>
                                        </td>
                                        <td>
                                            <div className={styles.action_button} onClick={() => handleDelete(user)}>
                                                <GiTrashCan size={20} />
                                                <span>
                                                    <SearchableText text="Delete" />
                                                </span>
                                            </div>
                                        </td>
                                    </tr>
                                )
                            })
                        }
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default UsersPage;


function ConfirmDeleteModal({user, onConfirm}) {
    const {modal} = useAppContext()
    function handleDelete() {
        onConfirm(user)
        modal.close()
    }
    return (
        <div>
            <h2>Are you sure you want to delete {user.name} {user.surname}?</h2>
            <div className={styles.buttons} style={{marginTop: "0.75rem"}}>
                <div>
                    <button type='submit' onClick={handleDelete}>Yes</button>
                    <button onClick={modal.close}>No</button>
                </div>
            </div>
        </div>
    )
}

function EditUserModal({user, onConfirm}) {
    const {modal} = useAppContext()
    const [currentStep, setCurrentStep] = useState(0)
    const [formData, setFormData] = useState({
        name: { value: user.name, error: false}, 
        surname: { value: user.surname, error: false}, 
        email: { value: user.email, error: false}, 
        username: { value: user.username, error: false},  
        address: { value: user.address, error: false}, 
        profession: { value: user.profession, error: false}, 
        phone: { value: user.phone, error: false}, 
        birthday: { value: user.dateOfBirth, error: false }
    })

    function handleSubmit(event) {
        event.preventDefault();
        if(
            (formData.name.error || formData.surname.error || formData.email.error || formData.username.error) || 
            (formData.address.error || formData.profession.error || formData.phone.error || formData.birthday.error) 
        ) {
            toast.error("Please fill in all required fields.");
            return;
        }
        const newUser = new User(user.id, formData.username.value, user.password, formData.name.value, formData.surname.value, formData.email.value, formData.birthday.value, formData.address.value, formData.phone.value, formData.profession.value);
        onConfirm(newUser);
        modal.close()
    }

    function handleNext() {
        if(currentStep === 1) return;
        setCurrentStep(currentStep + 1);
    }
    function handlePrevious() {
        if(currentStep === 0) return;
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

    return (
        <form className={styles.form} onSubmit={handleSubmit}>
            <h2>Edit user {currentStep+1}/2</h2>
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
                </div>
                
                <div className={styles.inputs} style={{
                    transform: `translateX(-${(currentStep) * 100}%) translateY(-50%)`,
                    position: "absolute",
                    right: "-100%",
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
                    <button type="submit">Save</button>
                    <button type="button" onClick={modal.close}>Cancel</button>
                </div>
                <div>
                    {
                        currentStep > 0 && <button type="button" onClick={handlePrevious}>Back</button>
                    }
                    {
                        currentStep < 1 && <button type="button" onClick={handleNext}>Next</button>
                    }
                </div>
            </div>
        </form>
    );
}