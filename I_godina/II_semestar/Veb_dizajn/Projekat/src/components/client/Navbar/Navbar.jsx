import React, {useState, useRef, useEffect} from 'react';
import { Link } from 'react-router-dom';
import styles from "./Navbar.module.css"
import useWindowSize from "../../../hooks/useWindowSize";
import { AiOutlineMenu } from "@react-icons/all-files/ai/AiOutlineMenu";
import { AiOutlineCloseCircle } from "@react-icons/all-files/ai/AiOutlineCloseCircle";
import { AiOutlineSearch } from "@react-icons/all-files/ai/AiOutlineSearch"
import Sidebar from './Sidebar';
import { useAppContext } from '../../../context/contextProvider';
import { Login, Register, loginWrapperClassName, registerWrapperClassName } from '../../common';
import toast from 'react-hot-toast';

const Navbar = () => {
    const windowSize = useWindowSize();
    const [searchActive, setSearchActive] = useState(false);
    const [inputValue, setInputValue] = useState("");
    const [menuActive, setMenuActive] = useState(false);
    const [menuHeight, setMenuHeight] = useState(0);
    const inputRef = useRef();
    const navRef = useRef();
    const {modal, setSearchText, setNavHeight, user, setUser} = useAppContext();
    

    useEffect(() => {
        if (!searchActive) {
            setInputValue("");
        }
    }, [searchActive])

    useEffect(() => {
        if (windowSize.width > 600) {
            setMenuActive(false);
        }
    }, [windowSize])

    useEffect(() => {
        setMenuHeight(navRef.current?.getBoundingClientRect()?.height ?? 0);
        setNavHeight(navRef.current?.getBoundingClientRect()?.height ?? 0);
    }, [navRef.current])

    useEffect(() => {
        setSearchText(inputValue);
    }, [inputValue])

    function loginClick() {
        modal.open(<Login />, {contentWrapperClassName: loginWrapperClassName})
    }

    function registerClick() {
        modal.open(<Register />, {contentWrapperClassName: registerWrapperClassName})
    }

    function logoutClick() {
        setUser(null);
        toast.success("Successfully logged out!\nGoodbye! See you soon!");
    }

    return (
        <nav ref={navRef} className={`${styles.navbar} ${menuActive ? styles.active_menu : ""}`}>
            <div>
                <Link title="FestiPlan Homepage" to="/" className={styles.block}>
                    <img className={styles.logo} src="/Logo-no-slogan-horizontal.svg" alt="Logo" />
                </Link>
            </div>
            <div className={styles.links_group}>
                {
                    !windowSize.width || windowSize.width > 600 ? (
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
                            <li className={`${styles.link} ${searchActive ? styles.search_active_other : ""}`}> <Link to="/admin">Admin</Link> </li>
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
                                <input onBlur={() => {setSearchActive(!!inputValue);}} ref={inputRef} value={inputValue} onChange={e => setInputValue(e.target.value)} type="text" className={`${styles.search_input} ${searchActive ? styles.search_input_active : ""}`} />
                            </li>
                        </ul>
                    ) : (
                        menuActive ? (
                            <AiOutlineCloseCircle onClick={() => setMenuActive(false)} title="Close menu" size={30} className={`pointer ${styles.block}`} />
                        ) : (
                            <AiOutlineMenu onClick={() => setMenuActive(true)} title="Open menu" size={30} className={`pointer ${styles.block}`} />
                        )
                    )
                }
            </div>
            <Sidebar {...{
                 searchActive, setSearchActive, inputValue, setInputValue, inputRef, menuActive, setMenuActive,
                 active: menuActive, height: `calc(100vh - ${menuHeight}px)`, width: (menuActive ? windowSize.width : 0)
            }} />
        </nav>
    );
};

export default Navbar;
