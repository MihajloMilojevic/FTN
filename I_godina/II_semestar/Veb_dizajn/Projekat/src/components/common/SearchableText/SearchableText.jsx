import { useAppContext } from "../../../context/contextProvider"
import styles from "./SearchableText.module.css"

function splitText(searchText, text) {
    const data = [];
    let index;
    while ((index = text.toLowerCase().indexOf(searchText.toLowerCase())) > -1) {
        if(index > 0) 
            data.push({highlighted: false, text: text.substring(0, index)});
        data.push({highlighted: true, text: text.substring(index, index + searchText.length)});
        text = text.substring(index + searchText.length);
    }
    if(text)
        data.push({highlighted: false, text});
    return data;
}

export default function SearchableText({text}) {

    const {searchText} = useAppContext();

    if(!searchText || !text.toLowerCase().includes(searchText.toLowerCase())) return (<>{text}</>)

    return (
        <>
            {
                splitText(searchText, text).map((data, index) => (
                    data.highlighted ? 
                    (<span key={index} className={styles.highlighted}>{data.text}</span>) : 
                    (<span key={index}>{data.text}</span>)
                ))
            }
        </>
    )
}