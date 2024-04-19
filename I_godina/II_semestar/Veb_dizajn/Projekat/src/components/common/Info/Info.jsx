import styles from "./Info.module.css"

export default function Info({left, right, customConnect = null, breakLeft=false, breakRight = true}) {

    return (
        <div className={styles.info}>
            <span className={`${breakLeft ? styles.break: styles.no_break}`}>
                {left}    
            </span> 
            {
                customConnect == null ? (
                    <div className={styles.connect} />
                ) : (
                    {customConnect}
                )
            }
            <span className={`${breakRight ? styles.break: styles.no_break}`}>
                {right}
            </span>
        </div>
    )
}