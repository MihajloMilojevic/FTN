import React, { useState } from 'react';
import useTitle from "../../hooks/useTitle";
import styles from "../../styles/admin/organizers.module.css"
import { useAppContext } from '../../context/contextProvider';
import {GiTrashCan} from "@react-icons/all-files/gi/GiTrashCan"
import {GiPencil} from "@react-icons/all-files/gi/GiPencil"
import {GrAdd} from "@react-icons/all-files/gr/GrAdd"
import toast from "react-hot-toast";
import { Organizer, User } from "../../models";
import { Link } from 'react-router-dom';
import { SearchableText } from '../../components/common';
import validateImageUrl from '../../utils/validateImageUrl';
import APIs from '../../api/API';

function OrganizersPage() {
    useTitle(`Organizers | FestiPlan`)
    const {data, setData, modal} = useAppContext();

    async function deleteOrganizer(organizer) {
        const deleted = await APIs.deleteOrganizer(organizer.id);
        if(!deleted) {
            toast.error("Failed to delete organizer.");
            return;
        }
        toast.success("Organizer deleted successfully.");
        setData({...data, organizers: data.organizers.filter(o => o.id !== organizer.id)})
    }

    function handleDelete(organizer) {
        modal.open(
            <ConfirmDeleteModal organizer={organizer} onConfirm={deleteOrganizer} />
        )
    }

    async function editOrganizer(newOrganizer) {
        const updated = await APIs.updateOrganizer(newOrganizer);
        if(!updated) {
            toast.error("Failed to update organizer.");
            return;
        }
        toast.success("Organizer updated successfully.");
        const copy = [...data.organizers];
        const index = copy.findIndex(o => o.id === newOrganizer.id);
        copy[index] = newOrganizer;
        setData({...data, organizers: copy});
    }

    function handleEdit(organizer) {
        modal.open(
            <OrganizerDataModal organizer={organizer} onConfirm={editOrganizer} />,
            {contentWrapperClassName: styles.wrapper    }
        )
    }

    async function createOrganizer(newOrganizer) {
        const {data: createdData, error} = await APIs.createOrganizer(newOrganizer);
        if(error) {
            toast.error("Failed to create organizer.");
            return;
        }
        toast.success("Organizer created successfully.");
        newOrganizer.festivalsId = createdData.name;
        setData({...data, organizers: [...data.organizers, newOrganizer]})
    }

    function handleCreate() {
        modal.open(
            <OrganizerDataModal onConfirm={createOrganizer} />,
            {contentWrapperClassName: styles.wrapper}
        )
    }

    return (
        <>
            <h1><SearchableText text="All festival organizers" /></h1>
            <button onClick={handleCreate} style={{maxWidth: 100}} className={styles.action_button}><GrAdd /> <SearchableText text="New" /> </button>
            <div className={styles.table_wrapper}>
                <table className={styles.table}>
                    <thead>
                        <tr>
                            <th><SearchableText text="Logo" /></th>
                            <th><SearchableText text="Name" /></th>
                            <th><SearchableText text="Address" /></th>
                            <th><SearchableText text="Phone" /></th>
                            <th><SearchableText text="Email" /></th>
                            <th><SearchableText text="Year" /></th>
                            <th><SearchableText text="Festivals" /></th>
                            <th colSpan={2}><SearchableText text="Actions" /></th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            data.organizers.map(organizer => {
                                return (
                                    <tr key={organizer.id}>
                                        <td>
                                            <div className={styles.logo_containter}>
                                                <img src={organizer.logo} alt={organizer.name} />
                                            </div>
                                        </td>
                                        <td><SearchableText text={organizer.name} /></td>
                                        <td><SearchableText text={organizer.address} /></td>
                                        <td><SearchableText text={organizer.contactPhone} /></td>
                                        <td><SearchableText text={organizer.email} /></td>
                                        <td><SearchableText text={organizer.yearOfEstablishment} /></td>
                                        <td><Link to={`/admin/organizers/${organizer.id}/festivals`}><SearchableText text={`${organizer.festivals.length} Festivals`} /></Link></td>
                                        <td>
                                            <div className={styles.action_button} onClick={() => handleEdit(organizer)}>
                                                <GiPencil size={20} />
                                                <span>
                                                    <SearchableText text="Edit" />
                                                </span>
                                            </div>
                                        </td>
                                        <td>
                                            <div className={styles.action_button} onClick={() => handleDelete(organizer)}>
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

export default OrganizersPage;


function ConfirmDeleteModal({organizer, onConfirm}) {
    const {modal} = useAppContext()
    function handleDelete() {
        onConfirm(organizer)
        modal.close()
    }
    return (
        <div>
            <h2>Are you sure you want to delete {organizer.name}?</h2>
            <div className={styles.buttons} style={{marginTop: "0.75rem"}}>
                <div>
                    <button type='submit' onClick={handleDelete}>Yes</button>
                    <button onClick={modal.close}>No</button>
                </div>
            </div>
        </div>
    )
}
function getInitialFormData(organizer) {
    if(organizer) return {
        name: {value: organizer.name, error: false},
        address: {value: organizer.address, error: false},
        contactPhone: {value: organizer.contactPhone, error: false},
        email: {value: organizer.email, error: false},
        yearOfEstablishment: {value: organizer.yearOfEstablishment, error: false},
        logo: {value: organizer.logo, error: false},
    }
    return {
        name: {value: "", error: null},
        address: {value: "", error: null},
        contactPhone: {value: "", error: null},
        email: {value: "", error: null},
        yearOfEstablishment: {value: "", error: null},
        logo: {value: "", error: null},
    }
}

function OrganizerDataModal({organizer, onConfirm}) {
    const {modal} = useAppContext()
    const [currentStep, setCurrentStep] = useState(0)
    const [formData, setFormData] = useState(getInitialFormData(organizer))

    async function handleSubmit(event) {
        event.preventDefault();
        if(
            formData.name.error == null || formData.address.error == null || formData.contactPhone.error == null || 
            formData.email.error == null || formData.yearOfEstablishment.error == null || formData.logo.error == null ||
            formData.name.error || formData.address.error || formData.contactPhone.error || 
            formData.email.error || formData.yearOfEstablishment.error || formData.logo.error
        ) {
            toast.error("Please fill in all required fields.");
            return;
        }
        const isImageValid = await validateImageUrl(formData.logo.value);
        if(!isImageValid) {
            toast.error("Invalid image url.");
            return;
        }
        const newOrganizer = new Organizer(
            organizer ? organizer.id : Math.random().toString(36), 
            formData.name.value, 
            formData.address.value, 
            formData.yearOfEstablishment.value, 
            formData.logo.value, 
            formData.contactPhone.value, 
            formData.email.value, 
            organizer ? organizer.festivals : [],
            organizer ? organizer.festivalsId : null
        );
        onConfirm(newOrganizer);
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
            <h2>{organizer ? "Edit" : "Create"} organizer {currentStep+1}/2</h2>
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
                        <label htmlFor="contactPhone">Phone:</label>
                        <input 
                            style={{
                                border: (formData.contactPhone.error != null ? 
                                    `2px solid ${(formData.contactPhone.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="tel" id="contactPhone" name="contactPhone" 
                            value={formData.contactPhone.value} onChange={handleOnlyRequiredChange}
                        />
                    </div>
                    <div>
                        <label htmlFor="yearOfEstablishment">Year of Establishment:</label>
                        <input 
                            style={{
                                border: (formData.yearOfEstablishment.error != null ? 
                                    `2px solid ${(formData.yearOfEstablishment.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="number" id="yearOfEstablishment" name="yearOfEstablishment" min={0} max={new Date().getFullYear()}
                            value={formData.yearOfEstablishment.value} onChange={handleOnlyRequiredChange}
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
                        <label htmlFor="logo">Logo:</label>
                        <input 
                            style={{
                                border: (formData.logo.error != null ? 
                                    `2px solid ${(formData.logo.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="text" id="logo" name="logo"
                            value={formData.logo.value} onChange={handleOnlyRequiredChange}
                        />
                    </div>
                    <div className={styles.form_logo}>
                        <img src={formData.logo.error || formData.logo.error == null ? "/no-image.svg" : formData.logo.value} alt="Invalid url" />
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