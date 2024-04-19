import React from "react";
import styles from "./CustomCheckbox.module.css"

export default function CustomCheckbox({size, ...props}) {
    return (
        <div role="checkbox" className={styles.wrapper}>
            <input type="checkbox" {...props}/>
            <div className={styles.outer} style={{width: size, height: size}}>
                {props.checked && <div className={styles.inner} />}
            </div>
        </div>
    )
}