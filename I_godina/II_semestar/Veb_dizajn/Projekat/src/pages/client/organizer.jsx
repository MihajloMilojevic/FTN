import React, { useMemo, useState } from 'react';
import { useParams } from 'react-router-dom';
import useTitle from "../../hooks/useTitle";
import { useAppContext } from '../../context/contextProvider';
import NotFound from '../404';
import { FestivalCard, HeroSection } from '../../components/client';
import { CardList } from '../../components/common';
import styles from "../../styles/client/organizer.module.css"
import { CustomCheckbox, Info, SearchableText } from '../../components/common';
import {BsFilter} from "@react-icons/all-files/bs/BsFilter"
import { FestivalTransportations, FestivalTypes } from '../../models/festival';

const initialFilters = {name: "", types: [], transportations: [], maxPrice: "", minPrice: "", maxPerson: ""}

function OrganizerPage() {
    const {data} = useAppContext();
    const [showFilters, setShowFilters] = useState(false)
    const {organizerId} = useParams();
    const organizer = useMemo(() => data.organizers.find(o => o.id === organizerId), [data, organizerId]);
    useTitle(`${organizer?.name ?? "Not Found"} | FestiPlan`)
    const [filters, setFilters] = useState(initialFilters)
    // console.log(organizer)
    function handleSimpleChange(e) {
        setFilters({...filters, [e.target.name]: e.target.value})
    }
    function handleCheckChange(e) {
        const {name, value, checked} = e.target;
        if(checked) {
            setFilters({...filters, [name]: [...filters[name], value]})
        }
        else {
            setFilters({...filters, [name]: filters[name].filter(txt => txt !== value)})
        }
    }
    function filterCheck(festival) {
        if(filters.name.trim() && !festival.name.toLowerCase().includes(filters.name.toLowerCase().trim())) return false;
        if(filters.maxPerson && parseInt(filters.maxPerson) && festival.maxPerson > parseInt(filters.maxPerson)) return false;
        if(filters.minPrice && parseInt(filters.minPrice) && festival.price < parseInt(filters.minPrice)) return false;
        if(filters.maxPrice && parseInt(filters.maxPrice) && festival.price > parseInt(filters.maxPrice)) return false;
        if(filters.types.length && !filters.types.includes(festival.type)) return false;
        if(filters.transportations.length && !filters.transportations.includes(festival.transportation)) return false;
        return true;
    }

    if (!organizer) 
        return <NotFound url="/" />
    return (
        <div>
            <HeroSection imageSrc={organizer.logo}>
                <h1><SearchableText text={organizer.name} /></h1>
            </HeroSection>
            <div className={styles.page}>
                <h2 className={styles.h2}><SearchableText text="Basic information:" /></h2>
                <div className={styles.info}>
                    <Info 
                        left={<SearchableText text="Address:" />}
                        breakLeft={false}
                        right={<SearchableText text={organizer.address} />}
                        breakRight={true}
                    />
                    <Info 
                        left={<SearchableText text="Email: " />}
                        breakLeft={false}
                        right={<a href={`mailto:${organizer.email}`}>{<SearchableText text={organizer.email}/>}</a>}
                        breakRight={true}
                    />
                    <Info 
                        left={<SearchableText text="Phone: " />}
                        breakLeft={false}
                        right={<a href={`tel:${organizer.contactPhone}`}>{<SearchableText text={organizer.contactPhone} />}</a>}
                        breakRight={true}
                    />
                    <Info 
                        left={<SearchableText text="Year of Establishment: " />}
                        breakLeft={true}
                        right={<SearchableText text={organizer.yearOfEstablishment} />}
                        breakRight={true}
                    />
                </div>
                <div className={styles.header_filter}>
                    <h2 className={styles.h2}><SearchableText text="Festivals:" /></h2>
                    <div className={styles.filters_button}  onClick={() => setShowFilters(prev => !prev)} >
                        <BsFilter size={40} />
                        <span>Filter</span>
                    </div>
                </div>
                <div className={`${styles.filters} ${showFilters ? styles.visible : ""}`}>
                    <div>
                        <label htmlFor="name">Name: </label>
                        <input type="text" id="name" name="name" value={filters.name} onChange={handleSimpleChange} />
                    </div>
                    <div>
                        <label>Type: </label>
                        {
                            FestivalTypes.values().map(type => (
                                <label key={type} htmlFor={`type-${type}`}>
                                    <CustomCheckbox size={25} name="types" id={`type-${type}`} checked={filters.types.includes(type)} value={type} onChange={handleCheckChange}  />
                                    <span>{type}</span>
                                </label>
                            ))
                        }
                    </div>
                    <div>
                        <label>Transportation: </label>
                        {
                            FestivalTransportations.values().map(trans => (
                                <label key={trans} htmlFor={`trans-${trans}`}>
                                    <CustomCheckbox  size={25} name="transportations" id={`trans-${trans}`} checked={filters.transportations.includes(trans)} value={trans} onChange={handleCheckChange} />
                                    <span>{trans}</span>
                                </label>
                            ))
                        }
                    </div>
                    <div>
                        <label htmlFor='min-price'>Minimum price: </label>
                        <input type="number" name="minPrice" id="min-price" min={0} value={filters.minPrice} onChange={handleSimpleChange} />
                    </div>
                    <div>
                        <label htmlFor='max-price'>Maximum price: </label>
                        <input type="number" name="maxPrice" id="max-price" min={0} value={filters.maxPrice} onChange={handleSimpleChange} />
                    </div>
                    <div>
                        <label htmlFor='max-people'>Maximum number of people: </label>
                        <input type="number" name="maxPerson" id="max-people" min={0} value={filters.maxPerson} onChange={handleSimpleChange} />
                    </div>
                </div>
                <CardList data={organizer.festivals.filter(filterCheck).map(f => ({...f, organizerId}))} CardComponent={FestivalCard} />
            </div>
        </div>
    );
}

export default OrganizerPage;