import React from 'react';
import styles from "./CardList.module.css";

function Cardlist({data, CardComponent, horizontal}) {
    return (
        <div className={`${styles.list} ${horizontal ? styles.horizontal : ""}`}>
            {
                data.map((item, index) => (
                    <CardComponent key={item?.id ?? (index+1)} item={item} />
                ))
            }
        </div>
    );
}

export default Cardlist;