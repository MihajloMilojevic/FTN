import * as Models from "../models";
import json_data from "../data/organizatori_festivala_engleski.json";

export default class APIs {
    static baseurl = "https://festiplan-wd-project-default-rtdb.europe-west1.firebasedatabase.app/"
    //////////////////////////////   DATA   //////////////////////////////
    static parseData(data) {
        const result = {
            organizers: [],
            users: []
        };
        for (const organizerId in data.festivalOrganizers) {
            const organizer = data.festivalOrganizers[organizerId];
            const festivals = [];
            for (const festivalId in data[organizer.festivals]) {
                const festival = data[organizer.festivals][festivalId];
                festivals.push(
                    new Models.Festival(
                        festivalId, 
                        festival.name, 
                        festival.description, 
                        festival.images, 
                        festival.type, 
                        festival.transportation, 
                        festival.price, 
                        festival.maxPerson
                ));
            }
            result.organizers.push(
                new Models.Organizer(
                    organizerId, 
                    organizer.name, 
                    organizer.address, 
                    organizer.yearOfEstablishment, 
                    organizer.logo, 
                    organizer.contactPhone, 
                    organizer.email, 
                    festivals,
                    organizer.festivals
                ));
        }
        for (const userId in data.users) {
            const user = data.users[userId];
            result.users.push(
                new Models.User(
                    userId,
                    user.username, 
                    user.password, 
                    user.name, 
                    user.surname, 
                    user.email, 
                    user.dateOfBirth, 
                    user.address, 
                    user.phone, 
                    user.profession
                ));
        }
        return result;
    }
    static async getData() {
        try {
            const response = await fetch(`${APIs.baseurl}/data.json`);
            const data = await response.json();
            return {data: APIs.parseData(data), error: null};
        }
        catch (error) {
            console.error("API.getData", error);
            return {data: null, error: error};
        }
    }
    static async resetData() {
        try {
            const response = await fetch(`${APIs.baseurl}/data.json`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(json_data.data)
            });  
            if (!response.ok) {
                console.error("API.resetData", response);
                return {data: null, error: response};
            }
            return {data: APIs.parseData(json_data.data), error: null};
        }
        catch(error) {
            console.error("API.resetData", error);
            return {data: null, error: error};
        }
    }
    //////////////////////////////   USERS   //////////////////////////////
    static async deleteUser(userId) {
        try {
            const response = await fetch(`${APIs.baseurl}/data/users/${userId}.json`, {
                method: "DELETE"
            });
            if (!response.ok) {
                console.error("API.deleteUser", response);
                return false;
            }
            return true;
        }
        catch(error) {
            console.error("API.deleteUser", error);
            return false;
        }
    }
    static async updateUser(user) {
        try {
            const response = await fetch(`${APIs.baseurl}/data/users/${user.id}.json`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(user.toDb())
            });
            if (!response.ok) {
                console.error("API.updateUser", response);
                return false;
            }
            return true;
        }
        catch(error) {
            console.error("API.updateUser", error);
            return false;
        }
    }
    static async createUser(user) {
        try {
            const response = await fetch(`${APIs.baseurl}/data/users.json`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(user.toDb())
            });
            if (!response.ok) {
                console.error("API.createUser", response);
                return {data: null, error: response};
            }
            return {data: await response.json(), error: null};
        }
        catch(error) {
            console.error("API.createUser", error);
            return {data: null, error: error};
        }
    }
    //////////////////////////////   ORGANIZERS   //////////////////////////////
    static async deleteOrganizer(organizerId) {
        try {
            const response = await fetch(`${APIs.baseurl}/data/festivalOrganizers/${organizerId}.json`, {
                method: "DELETE"
            });
            if (!response.ok) {
                console.error("API.deleteOrganizer", response);
                return false;
            }
            return true;
        }
        catch(error) {
            console.error("API.deleteOrganizer", error);
            return false;
        }
    }
    static async updateOrganizer(organizer) {
        try {
            const response = await fetch(`${APIs.baseurl}/data/festivalOrganizers/${organizer.id}.json`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(organizer.toDb())
            });
            if (!response.ok) {
                console.error("API.updateOrganizer", response);
                return false;
            }
            return true;
        }
        catch(error) {
            console.error("API.updateOrganizer", error);
            return false;
        }
    }
    static async createOrganizerFestivals() {
        try {
            const response = await fetch(`${APIs.baseurl}/data.json`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: "{}"
            });
            if (!response.ok) {
                console.error("API.createOrganizerFestivals", response);
                return {data: null, error: response};
            }
            return {data: await response.json(), error: null};
        }
        catch(error) {
            console.error("API.createOrganizerFestivals", error);
            return {data: null, error: error};
        }
    }
    static async createOrganizer(organizer) {
        try {
            const festivalObj = await APIs.createOrganizerFestivals();
            if (festivalObj.error) {
                return festivalObj;
            }
            organizer.festivalsId = festivalObj.data.name;
            const response = await fetch(`${APIs.baseurl}/data/festivalOrganizers.json`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(organizer.toDb())
            });
            if (!response.ok) {
                console.error("API.createOrganizer", response);
                return {data: null, error: response};
            }
            return {data: await response.json(), error: null};
        }
        catch(error) {
            console.error("API.createOrganizer", error);
            return {data: null, error: error};
        }
    }
    //////////////////////////////   FESTIVALS   //////////////////////////////
    static async deleteFestival(organizerFestivalsId, festivalId) {
        try {
            const response = await fetch(`${APIs.baseurl}/data/${organizerFestivalsId}/${festivalId}.json`, {
                method: "DELETE"
            });
            if (!response.ok) {
                console.error("API.deleteFestival", response);
                return false;
            }
            return true;
        }
        catch(error) {
            console.error("API.deleteFestival", error);
            return false;
        }
    }
    static async updateFestival(organizerFestivalsId, festival) {
        try {
            const response = await fetch(`${APIs.baseurl}/data/${organizerFestivalsId}/${festival.id}.json`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(festival.toDb())
            });
            if (!response.ok) {
                console.error("API.updateFestival", response);
                return false;
            }
            return true;
        }
        catch(error) {
            console.error("API.updateFestival", error);
            return false;
        }
    }
    static async createFestival(organizerFestivalsId, festival) {
        try {
            const response = await fetch(`${APIs.baseurl}/data/${organizerFestivalsId}.json`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(festival.toDb())
            });
            if (!response.ok) {
                console.error("API.createFestival", response);
                return {data: null, error: response};
            }
            return {data: await response.json(), error: null};
        }
        catch(error) {
            console.error("API.createFestival", error);
            return {data: null, error: error};
        }
    }  
}