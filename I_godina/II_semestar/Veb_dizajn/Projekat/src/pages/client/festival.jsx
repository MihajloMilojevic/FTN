import React, {useMemo, useState} from 'react';
import useTitle from "../../hooks/useTitle";
import { Link, useParams } from 'react-router-dom';
import {FestivalTypeIcon, FestivalTransportationIcon} from '../../components/common';
import NotFound from '../404';
import { useAppContext } from '../../context/contextProvider';
import styles from "../../styles/client/festival.module.css";
import { Info, SearchableText } from '../../components/common';
import {GrNext} from "@react-icons/all-files/gr/GrNext"
import {GrPrevious} from "@react-icons/all-files/gr/GrPrevious"
import {GiTakeMyMoney} from "@react-icons/all-files/gi/GiTakeMyMoney"
import {HiOutlineUserGroup} from "@react-icons/all-files/hi/HiOutlineUserGroup"


function FestivalPage() {

    const [activeIndex, setActiveIndex] = useState(0);

    const {data} = useAppContext();
    const {organizerId, festivalId} = useParams();
    const organizer = useMemo(() => data.organizers.find(o => o.id === organizerId), [data, organizerId]);
    const festival = useMemo(() => {
        if (!organizer) return null;
        return organizer.festivals.find(f => f.id === festivalId);
    }, [organizerId, organizer, festivalId]);
    useTitle(`${festival?.name ?? "NotFound"} | FestiPlan`)
    if (!organizer || !festival) 
        return <NotFound url="/" />
    return (
        <div>
            <div className={styles.container}>
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
                        <GrPrevious size={25} />
                    </button>
                    <button 
                        className={styles.btn} 
                        onClick={() => setActiveIndex(prev => (prev + 1) % festival.images.length)}
                    >
                        <GrNext size={25} />
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
                <div className={styles.content}>
                    <h1><SearchableText text={festival.name} /></h1>
                    <p className={styles.desc}><SearchableText text={festival.description} /></p>
                    <div className={styles.info}>
                        <Info 
                            left={<SearchableText text="Organizer: " />}
                            breakLeft={false}
                            right={
                                <Link to={`/organizers/${organizerId}`}>
                                    <SearchableText text={organizer.name} />
                                </Link>
                            }
                            breakRight={true}
                        />
                        <Info 
                            left={<SearchableText text="Type: " />}
                            breakLeft={false}
                            right={
                                <div className={styles.icon_text}>
                                    <FestivalTypeIcon type={festival.type} size={25} /> 
                                    <SearchableText text={festival.type} />
                                </div>
                            }
                            breakRight={true}
                        />
                        <Info 
                            left={<SearchableText text="Transportation: " />}
                            breakLeft={false}
                            right={
                                <div className={styles.icon_text}>
                                    <FestivalTransportationIcon transportation={festival.transportation} size={25} /> 
                                    <SearchableText text={festival.transportation} />
                                </div>
                            }
                            breakRight={true}
                        />
                        <Info 
                            left={<SearchableText text="Price: " />}
                            breakLeft={false}
                            right={
                                <div className={styles.icon_text}>
                                    <GiTakeMyMoney size={25} /> 
                                    <SearchableText text={`${festival.price} rsd`} />
                                </div>
                            }
                            breakRight={true}
                        />
                        <Info 
                            left={<SearchableText text="People: " />}
                            breakLeft={false}
                            right={
                                <div className={styles.icon_text}>
                                    <HiOutlineUserGroup size={25} /> 
                                    <SearchableText text={`${festival.maxPerson}`} />
                                </div>
                            }
                            breakRight={true}
                        />
                    </div>
                </div>
            </div>
        </div>
    );
}

export default FestivalPage;