import React from "react";
import {MdError} from "@react-icons/all-files/md/MdError"
import {GiFilmProjector} from "@react-icons/all-files/gi/GiFilmProjector"
import {GiMusicalNotes} from "@react-icons/all-files/gi/GiMusicalNotes"
import {GiMeal} from "@react-icons/all-files/gi/GiMeal"
import {IoSchool} from "@react-icons/all-files/io5/IoSchool"
import {GiPalette} from "@react-icons/all-files/gi/GiPalette"

export default function FestivalTypeIcon({type, ...props}) {
    switch (type.toLowerCase()) {
        case "film":
            return <GiFilmProjector {...props} />
        case "music":
            return <GiMusicalNotes {...props} />
        case "food":
            return <GiMeal {...props} />
        case "education":
            return <IoSchool {...props} />
        case "art":
            return <GiPalette {...props} />
        default:
            return <MdError {...props} />
    }
}