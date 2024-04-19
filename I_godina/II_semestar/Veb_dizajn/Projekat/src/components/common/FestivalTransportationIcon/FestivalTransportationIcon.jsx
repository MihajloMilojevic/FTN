import React from "react";
import {MdError} from "@react-icons/all-files/md/MdError"
import {GiBus} from "@react-icons/all-files/gi/GiBus"
import {GiCommercialAirplane} from "@react-icons/all-files/gi/GiCommercialAirplane"
import {FaCarSide} from "@react-icons/all-files/fa/FaCarSide"
import {IoSchool} from "@react-icons/all-files/io5/IoSchool"
import {GiPalette} from "@react-icons/all-files/gi/GiPalette"

export default function FestivalTransportationIcon({transportation, ...props}) {
    switch (transportation.toLowerCase()) {
        case "bus":
            return <GiBus {...props} />
        case "plane":
            return <GiCommercialAirplane {...props} />
        case "own":
            return <FaCarSide {...props} />
        default:
            return <MdError {...props} />
    }
}