import React, {useRef} from 'react';
import { Link } from 'react-router-dom';
import { AiOutlineSearch } from "@react-icons/all-files/ai/AiOutlineSearch"
import styles from "./Sidebar.module.css";
import { Login, Register, loginWrapperClassName, registerWrapperClassName } from '../../common';
import { useAppContext } from '../../../context/contextProvider';
import toast from 'react-hot-toast';


function Sidebar({active, height, width, searchActive, setSearchActive, inputValue, setInputValue, menuActive, setMenuActive}) {
    const inputRef = useRef();
    const {modal, user, setUser} = useAppContext();
    function close() {
        setMenuActive(false)
    }
    function loginClick() {
        modal.open(<Login />, {contentWrapperClassName: loginWrapperClassName})
        close();
    }

    function logoutClick() {
        setUser(null);
        toast.success("Successfully logged out!\nGoodbye! See you soon!");
        close();
    }

    function registerClick() {
        modal.open(<Register />, {contentWrapperClassName: registerWrapperClassName})
        close();
    }

    return (
        <div 
            className={`${styles.sidebar} ${active ? styles.active : ""}`} 
            style={{height, width}}
        >
            <ul className={styles.list}>
                {
                    user ? (
                        <>
                            <li className={`${styles.user} ${searchActive ? styles.search_active_other : ""}`}>{user.name}</li>
                            <li onClick={logoutClick} className={`${styles.link} ${searchActive ? styles.search_active_other : ""}`}>Logout</li>
                        </>
                    ) : (
                        <>
                            <li onClick={loginClick} className={`${styles.link} ${searchActive ? styles.search_active_other : ""}`}>Login</li>
                            <li onClick={registerClick} className={`${styles.link} ${searchActive ? styles.search_active_other : ""}`}>Register</li>
                        </>
                    )
                }
                <li onClick={close} className={`${styles.link}`}><Link to="/">Client</Link> </li>
                <li 
                    className={`
                        ${styles.link} 
                        ${styles.block} 
                        ${styles.search}
                        ${searchActive ? styles.search_active_parent : ""}
                    `}
                >
                    <div
                        className={`
                            ${styles.link} 
                            ${styles.block} 
                            ${styles.search} 
                            ${searchActive ? styles.search_active : ""}
                        `}
                        onClick={() => {setSearchActive(true); inputRef.current.focus()}}
                    >
                        {
                            !inputValue && (
                                <>
                                    <AiOutlineSearch title="Search on page" size={25} className={`pointer ${styles.block}`} />
                                    { searchActive ? "Search on page" : "Search"}
                                </>
                            )
                        }
                    </div>
                    <input onBlur={() => setSearchActive(!!inputValue)} ref={inputRef} value={inputValue} onChange={e => setInputValue(e.target.value)} type="text" className={`${styles.search_input} ${searchActive ? styles.search_input_active : ""}`} />
                </li>
                </ul>
        </div>
    );
};

export default Sidebar;