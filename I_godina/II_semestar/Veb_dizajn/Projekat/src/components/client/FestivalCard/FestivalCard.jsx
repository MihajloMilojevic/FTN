import React, {useState} from 'react';
import styles from "./Festival.module.css";
import { Link } from 'react-router-dom';
import { SearchableText } from '../../common';
import FestivalTypeIcon from "../../common/FestivalTypeIcon/FestivalTypeIcon";
import FestivalTransportationIcon from '../../common/FestivalTransportationIcon/FestivalTransportationIcon';
import {GiTakeMyMoney} from "@react-icons/all-files/gi/GiTakeMyMoney"
import {HiOutlineUserGroup} from "@react-icons/all-files/hi/HiOutlineUserGroup"

function FestivalCard({item: festival}) {
    const [activeImage, setActiveImage] = useState(0);
    const [intervalObj, setIntervalObj] = useState(null);
    function onHover() {
        if (festival.images.length > 1) {
            const interval = setInterval(() => {
                setActiveImage((prev) => (prev + 1) % festival.images.length);
            }, 1000 * 1.5);
            setIntervalObj(interval);
        }
    }
    function onHoverEnd() {
        clearInterval(intervalObj);
        setActiveImage(0);
        setIntervalObj(null);
    }

    return (
        <Link to={`/organizers/${festival.organizerId}/festivals/${festival.id}`}>
            <div className={styles.card} onMouseEnter={onHover} onMouseLeave={onHoverEnd}>
                <div>
                    <div className={styles.image_container}>
                        {
                            festival.images.map((image, index) => 
                                <img key={index} style={{zIndex: index+2}} src={image} alt={festival.name + (index + 1)} className={`${styles.image} ${index === activeImage ? styles.active : ""}`}/>
                            )
                        }
                    </div>
                    <h2 className={styles.text}><SearchableText text={festival.name} /></h2>
                </div>
                <div className={styles.taglist}>
                    <p className={styles.tag}><GiTakeMyMoney size={20} /><SearchableText text={festival.price + " rsd"} /></p>
                    <p className={styles.tag}><HiOutlineUserGroup size={20} /><SearchableText text={festival.maxPerson.toString()} /></p>
                    <p className={styles.tag}><FestivalTransportationIcon transportation={festival.transportation} size={20} /><SearchableText text={festival.transportation} /></p>
                    <p className={styles.tag}><FestivalTypeIcon type={festival.type} size={20} /><SearchableText text={festival.type} /></p>
                </div>
            </div>
        </Link>
    );
}

export default FestivalCard;