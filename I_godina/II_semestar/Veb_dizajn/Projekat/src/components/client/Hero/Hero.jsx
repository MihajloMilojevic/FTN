import React, { useEffect, useState } from "react";
import styles from "./Hero.module.css"
import { useAppContext } from "../../../context/contextProvider";
import { Fireworks } from 'fireworks/lib/react'
import useWindowSize from "../../../hooks/useWindowSize";
import { SearchableText } from "../../common";

function HeroSection({imageSrc = "/hero-image.jpg", fireworks=false, children}) {
    const [showFireworks, setShowFireworks] = useState(fireworks);
    const {navHeight} = useAppContext();
    const windowSize = useWindowSize();
    useEffect(() => {
      function handleLeave() {
        setShowFireworks(false);
      }
      function handleEnter() {
        setShowFireworks(fireworks);
      }
      window.addEventListener("blur", handleLeave);
      window.addEventListener("focus", handleEnter);
      return () => {
        window.removeEventListener("blur", handleLeave);
        window.removeEventListener("focus", handleEnter);
      }
    }, [])
    let fxProps = {
        count: 3,
        interval: 1000,
        colors: ["#cc3333", "#4CAF50", "#81C784", "#FFD700", "#FF5722", "#FF69B4", "#FFA500", "#FFD700", "#FF69B4", "#FFA500"],
        calc: (props, i) => ({
          ...props,
          x: Math.random() * window.innerWidth,
          y: Math.random() * window.innerHeight,
          particleTimeout: 50000 //Math.random() * 700 + 300,
        })
      }
    return (
        <header className={styles.hero} style={{height: `calc(100vh - ${navHeight}px)`, paddingBottom: navHeight}}>
            <img src={imageSrc} className={styles.bg} />
            {children}
            { showFireworks && windowSize.width > 750 && <div style={{position: "absolute"}}><Fireworks  {...fxProps} /></div>}
        </header>
    )
}

export default HeroSection;