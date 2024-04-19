import React, { useRef, useState } from 'react';
import useTitle from "../../hooks/useTitle";
import {HeroSection, OrganizerCard} from '../../components/client';
import { CardList } from '../../components/common';
import { useAppContext } from '../../context/contextProvider';
import styles from "../../styles/client/homepage.module.css";
import { SearchableText } from '../../components/common';
import { AiOutlineSearch } from "@react-icons/all-files/ai/AiOutlineSearch"

function Homepage() {
    const { data } = useAppContext();
    const inputRef = useRef(null)
    const [filterText, setFilterText] = useState("")
    useTitle(`FestiPlan`)
    function organizerFilter(organizer) {
        if(!filterText) return true;
        return organizer.name.toLowerCase().includes(filterText.toLowerCase())
    }
    return (
        <div>
            <HeroSection imageSrc="/hero-image.jpg" fireworks>
                <h1><SearchableText text="FestiPlan" /></h1>
                <p><SearchableText text="Bringing festivities to life, one plan at the time!" /></p>
            </HeroSection>
            
            <div className={styles.organizers_list_container}>
                <h2><SearchableText text={"Check out our organizers"} /></h2>
                <div className={styles.filter_container}>
                    <div className={styles.input_field} onClick={() => inputRef.current.focus()}>
                        <AiOutlineSearch title="Search on page" size={25} className={`pointer ${styles.block}`} />
                        <input value={filterText} onChange={e => setFilterText(e.target.value)} ref={inputRef} placeholder="Filter organizers by name: " />
                    </div>
                </div>
                <CardList data={data.organizers.filter(organizerFilter)} CardComponent={OrganizerCard} />
            </div>
        </div>
    );
}

export default Homepage;