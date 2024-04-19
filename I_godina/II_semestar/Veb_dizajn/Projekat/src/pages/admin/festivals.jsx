import React, { useEffect, useMemo, useState } from 'react';
import { useParams } from 'react-router-dom';
import useTitle from "../../hooks/useTitle";
import { useAppContext } from '../../context/contextProvider';
import NotFound from '../404';
import {GiTrashCan} from "@react-icons/all-files/gi/GiTrashCan"
import {GiPencil} from "@react-icons/all-files/gi/GiPencil"
import {GrAdd} from "@react-icons/all-files/gr/GrAdd"
import {GrNext} from "@react-icons/all-files/gr/GrNext"
import { AiOutlineCloseCircle } from "@react-icons/all-files/ai/AiOutlineCloseCircle";
import {GrPrevious} from "@react-icons/all-files/gr/GrPrevious"
import toast from "react-hot-toast";
import { Organizer, User } from "../../models";
import { Link } from 'react-router-dom';
import { SearchableText } from '../../components/common';
import validateImageUrl from '../../utils/validateImageUrl';
import { FestivalTypeIcon, FestivalTransportationIcon } from '../../components/common';
import {GiTakeMyMoney} from "@react-icons/all-files/gi/GiTakeMyMoney"
import {HiOutlineUserGroup} from "@react-icons/all-files/hi/HiOutlineUserGroup"
import Festival, { FestivalTransportations, FestivalTypes } from '../../models/festival';
import styles from "../../styles/admin/festivals.module.css"
import useWindowSize from '../../hooks/useWindowSize';
import APIs from '../../api/API';

export default function OrganizersFestivalsPage() {
    const {data, setData, modal} = useAppContext();
    const {organizerId} = useParams();
    const organizer = useMemo(() => data.organizers.find(o => o.id === organizerId), [data, organizerId]);
    useTitle(`${organizer?.name + "'s Festivals" ?? "Not Found"} | FestiPlan`)

    if (!organizer) 
        return <NotFound url="/admin" />

    async function deleteFestival(festival) {
        const deleted = await APIs.deleteFestival(organizer.festivalsId, festival.id);
        if(!deleted) {
            toast.error("Failed to delete festival. Please try again later.");
            return;
        }
        toast.success("Festival deleted successfully.");
        organizer.festivals = organizer.festivals.filter(f => f.id !== festival.id);
        const copy = [...data.organizers];
        const index = copy.findIndex(o => o.id === organizer.id);
        copy[index] = organizer;
        setData({...data, organizers: copy});
    }

    function handleDelete(festival) {
        modal.open(
            <ConfirmDeleteModal festival={festival} onConfirm={deleteFestival} />
        )
    }

    async function editFestival(newFestival) {
        const updated = await APIs.updateFestival(organizer.festivalsId, newFestival);
        if(!updated) {
            toast.error("Failed to update festival. Please try again later.");
            return;
        }
        toast.success("Festival updated successfully.");
        const festivalsCopy = [...organizer.festivals];
        const festivalIndex = festivalsCopy.findIndex(f => f.id === newFestival.id);
        festivalsCopy[festivalIndex] = newFestival;
        organizer.festivals = festivalsCopy;
        const copy = [...data.organizers];
        const organizerIndex = copy.findIndex(o => o.id === organizer.id);
        copy[organizerIndex] = organizer;
        setData({...data, organizers: copy});
    }

    function handleEdit(festival) {
        modal.open(
            <FestivalDataModel festival={festival} onConfirm={editFestival} />,
            {contentWrapperClassName: styles.wrapper    }
        )
    }

    async function createFestival(newFestival) {
        const {data: createdData, error} = await APIs.createFestival(organizer.festivalsId, newFestival);
        if(error) {
            toast.error("Failed to create festival. Please try again later.");
            return;
        }
        newFestival.id = createdData.name;
        organizer.festivals.push(newFestival);
        const copy = [...data.organizers];
        const index = copy.findIndex(o => o.id === organizer.id);
        copy[index] = organizer;
        setData({...data, organizers: copy});
    }

    function handleCreate() {
        modal.open(
            <FestivalDataModel onConfirm={createFestival} />,
            {contentWrapperClassName: styles.wrapper}
        )
    }

    return (
        <>
            <h1><SearchableText text={`All ${organizer.name}'s Festivals`} /></h1>
            <button 
                onClick={handleCreate} 
                style={{maxWidth: 100}} 
                className={styles.action_button}
            >
                <GrAdd /> 
                <SearchableText text="New" />
            </button>
            <div className={styles.table_wrapper}>
                <table className={styles.table}>
                    <thead>
                        <tr>
                            <th><SearchableText text="Images" /></th>
                            <th><SearchableText text="Name" /></th>
                            <th><SearchableText text="Type" /></th>
                            <th><SearchableText text="Transportation" /></th>
                            <th><SearchableText text="Price" /></th>
                            <th><SearchableText text="Maximum People" /></th>
                            <th><SearchableText text="Description" /></th>
                            <th colSpan={2}><SearchableText text="Actions" /></th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            organizer.festivals.map(festival => {
                                return (
                                    <tr key={festival.id}>
                                        <td>
                                            <FestivalGallery festival={festival} />
                                        </td>
                                        <td><SearchableText text={festival.name} /></td>
                                        <td>
                                            <div className={styles.icon_text}>
                                                <FestivalTypeIcon type={festival.type} size={20} />
                                                <SearchableText text={festival.type} />
                                            </div>
                                        </td>
                                        <td>
                                            <div className={styles.icon_text}>
                                                <FestivalTransportationIcon transportation={festival.transportation} size={20} />
                                                <SearchableText text={festival.transportation} />
                                            </div>
                                        </td>
                                        <td>
                                            <div className={styles.icon_text}>
                                                <GiTakeMyMoney size={20} />
                                                <SearchableText text={festival.price} />
                                            </div>
                                        </td>
                                        <td>
                                            <div className={styles.icon_text}>
                                                <HiOutlineUserGroup size={20} />
                                                <SearchableText text={festival.maxPerson} />
                                            </div>
                                        </td>
                                        <td><SearchableText text={festival.description} /></td>
                                        <td>
                                            <div 
                                                className={styles.action_button} 
                                                onClick={() => handleEdit(festival)}
                                            >
                                                <GiPencil size={20} />
                                                <span>
                                                    <SearchableText text="Edit" />
                                                </span>
                                            </div>
                                        </td>
                                        <td>
                                            <div 
                                                className={styles.action_button} 
                                                onClick={() => handleDelete(festival)}
                                            >
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

function FestivalGallery({festival}) {
    
    const [activeIndex, setActiveIndex] = useState(0);
    return (
        <div className={styles.gallery}>
            {
                festival.images.map((image, index) => (
                    <img className={`${styles.image} ${index === activeIndex ? styles.active : ""}`} key={index} src={image} alt={festival.name + (index+1)} />
                ))
            }
            <button 
                className={styles.btn} 
                onClick={() => setActiveIndex(prev => (prev - 1 + festival.images.length) % festival.images.length)}
            >
                <GrPrevious size={15} />
            </button>
            <button 
                className={styles.btn} 
                onClick={() => setActiveIndex(prev => (prev + 1) % festival.images.length)}
            >
                <GrNext size={15} />
            </button>
            <div className={styles.circle_list}>
                {festival.images.map((_, index) => (
                    <button
                        key={index}
                        className={`${styles.circle} ${index == activeIndex ? styles.current : ""}`} 
                        onClick={() => setActiveIndex(index)}
                    />
                ))}
            </div>
        </div>
    )
}

function ConfirmDeleteModal({festival, onConfirm}) {
    const {modal} = useAppContext()
    function handleDelete() {
        onConfirm(festival)
        modal.close()
    }
    return (
        <div>
            <h2>Are you sure you want to delete {festival.name}?</h2>
            <div className={styles.buttons} style={{marginTop: "0.75rem"}}>
                <div>
                    <button type='submit' onClick={handleDelete}>Yes</button>
                    <button onClick={modal.close}>No</button>
                </div>
            </div>
        </div>
    )
}
function getInitialFormData(festival) {
    if(festival) return {
        name: {value: festival.name, error: false},
        description: {value: festival.description, error: false},
        maxPerson: {value: festival.maxPerson, error: false},
        price: {value: festival.price, error: false},
        type: {value: festival.type, error: false},
        transportation: {value: festival.transportation, error: false},
        images: {value: festival.images}
    }
    return {
        name: {value: "", error: null},
        description: {value: "", error: null},
        maxPerson: {value: "", error: null},
        price: {value: "", error: null},
        type: {value: "", error: null},
        transportation: {value: "", error: null},
        images: {value: []}
    }
}

function splitArray(arr, size) {
    const result = [];
    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }
    return result;
}

function FestivalDataModel({festival, onConfirm}) {

    const [SIZE, setSize] = useState(3);
    const {modal} = useAppContext()
    const [currentStep, setCurrentStep] = useState(0)
    const [formData, setFormData] = useState(getInitialFormData(festival))
    const [stepCount, setStepCount] = useState(3);
    const windowSize = useWindowSize();
    
    useEffect(() => {
        setStepCount(2 + Math.ceil(formData.images.value.length / SIZE) + (formData.images.value.length % SIZE === 0 ? 1 : 0));
    }, [formData.images.value])

    useEffect(() => {
        if(windowSize.width < 512) {
            setSize(1);
        }
        else if(windowSize.width < 768) {
            setSize(2);
        }
        else {
            setSize(3);
        }
        if(windowSize.height < 500) {
            setSize(1);
        }
    }, [windowSize])

    async function handleSubmit(event) {
        event.preventDefault();
        if(
            formData.name.error || formData.description.error || formData.maxPerson.error || 
            formData.price.error || formData.type.error || formData.transportation.error || !formData.images.value.every(Boolean) ||
            formData.name.error == null || formData.description.error == null || formData.maxPerson.error == null || 
            formData.price.error == null || formData.type.error == null || formData.transportation.error == null
        ) {
            toast.error("Please fill in all required fields.");
            return;
        }
        if(formData.images.value.length === 0) {
            toast.error("Please add at least one image.");
            return;
        }
        const areAllImagesValid = await Promise.all(formData.images.value.map(validateImageUrl));
        if(!areAllImagesValid.every(Boolean)) {
            toast.error("One or more images are invalid. Please check the urls and try again.");
            return;
        }
        const newFestival = new Festival(
            festival ? festival.id : Math.random().toString(36), 
            formData.name.value, 
            formData.description.value,
            formData.images.value,
            formData.type.value,
            formData.transportation.value,
            formData.price.value,
            formData.maxPerson.value 
        );
        onConfirm(newFestival);
        modal.close()
    }

    function handleNext() {
        if(currentStep === stepCount - 1) return;
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

    function removeImage(index) {
        const newImages = formData.images.value.filter((_, i) => i !== index);
        setFormData({...formData, images: {value: newImages, error: null}});
    }

    function addImage() {
        const newImages = [...formData.images.value, ""];
        setFormData({...formData, images: {value: newImages, error: null}});
    }

    return (
        <form className={styles.form} onSubmit={handleSubmit}>
            <h2>{festival ? "Edit" : "Create"} festival {currentStep+1}/{stepCount}</h2>
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
                        <label htmlFor="description">Description:</label>
                        <textarea 
                            style={{
                                border: (formData.description.error != null ? 
                                    `2px solid ${(formData.description.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            rows={10}
                            type="text" id="description" name="description" 
                            value={formData.description.value} onChange={handleOnlyRequiredChange} 
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
                        <label htmlFor="type">Type:</label>
                        <select 
                            style={{
                                border: (formData.type.error != null ? 
                                    `2px solid ${(formData.type.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            id="type" name="type" 
                            value={formData.type.value} onChange={handleOnlyRequiredChange}
                        >
                            <option value=""></option>
                            {
                                FestivalTypes.values().map(value => (
                                    <option key={value} value={value} >
                                        <SearchableText text={value} />
                                    </option>
                                ))
                            }
                        </select>
                    </div>
                    <div>
                        <label htmlFor="transportation">Transportation:</label>
                        <select 
                            style={{
                                border: (formData.transportation.error != null ? 
                                    `2px solid ${(formData.transportation.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            id="transportation" name="transportation" 
                            value={formData.transportation.value} onChange={handleOnlyRequiredChange}
                        >
                            <option value=""></option>
                            {
                                FestivalTransportations.values().map(value => (
                                    <option key={value} value={value} >
                                        <SearchableText text={value} />
                                    </option>
                                ))
                            }
                        </select>
                    </div>
                    <div>
                        <label htmlFor="price">Price:</label>
                        <input 
                            style={{
                                border: (formData.price.error != null ? 
                                    `2px solid ${(formData.price.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="number" id="price" name="price" min={0}
                            value={formData.price.value} onChange={handleOnlyRequiredChange}
                        />
                    </div>
                    <div>
                        <label htmlFor="maxPerson">Maximum Number Of People:</label>
                        <input 
                            style={{
                                border: (formData.maxPerson.error != null ? 
                                    `2px solid ${(formData.maxPerson.error ? "red" : "green")}` : 
                                    "none")
                            }}
                            type="number" id="maxPerson" name="maxPerson" min={0}
                            value={formData.maxPerson.value} onChange={handleOnlyRequiredChange}
                        />
                    </div>
                </div>
                {
                    splitArray(formData.images.value, SIZE).map((images, index) => (
                        <div key={index} className={styles.inputs} style={{
                            transform: `translateX(-${(currentStep) * 100}%) translateY(-50%)`,
                            position: "absolute",
                            right: `-${100*(index+2)}%`,
                            top: "50%"
                        }}>
                            {
                                images.map((image, i) => (
                                    <div key={i}>
                                        <label htmlFor={`image_${index * SIZE + i}`}>Image {index * SIZE + i + 1}:</label>
                                        <input 
                                            type="text" id={`image_${index * SIZE + i}`} name={`image_${index * SIZE + i}`}
                                            value={image} onChange={e => {
                                                const newImages = [...formData.images.value];
                                                newImages[index * SIZE + i] = e.target.value;
                                                setFormData({...formData, images: {value: newImages}});
                                            }}
                                        />
                                        <div className={styles.preview}>
                                            <div>
                                                <img src={image ? image : "/no-image.svg"} alt={`Invalid url`} />
                                            </div>
                                            <button className={styles.close} type="button" onClick={() => removeImage(index*SIZE+i)}>
                                                <AiOutlineCloseCircle size={20} />
                                            </button>
                                        </div>
                                    </div>
                                ))
                            }
                            {
                                images.length < SIZE && (
                                    <button type="button" onClick={addImage} className={styles.action_button}>
                                        <GrAdd size={20} />
                                        <span>
                                            <SearchableText text="Add Image" />
                                        </span>
                                    </button>
                                )
                            }
                        </div>
                    ))
                }
                {
                    formData.images.value.length % SIZE === 0 && (
                        <div className={styles.inputs} style={{
                            transform: `translateX(-${(currentStep) * 100}%) translateY(-50%)`,
                            position: "absolute",
                            right: `-${100*(parseInt(formData.images.value.length / SIZE)+2)}%`,
                            top: "50%"
                        }}>
                            <button type="button" onClick={addImage} className={styles.action_button}>
                                <GrAdd size={20} />
                                <span>
                                    <SearchableText text="Add Image" />
                                </span>
                            </button>
                        </div>
                    )
                }
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
                        currentStep < stepCount-1 && <button type="button" onClick={handleNext}>Next</button>
                    }
                </div>
            </div>
        </form>
    );
}
