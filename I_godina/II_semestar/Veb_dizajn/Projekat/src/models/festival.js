export default class Festival {
    constructor(id, name, description, images, type, transportation, price, maxPerson) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.images = images;
        this.type = type;
        this.transportation = transportation;
        this.price = price;
        this.maxPerson = maxPerson;
    }
    toDb() {
        return {
            name: this.name,
            description: this.description,
            images: this.images,
            type: this.type,
            transportation: this.transportation,
            price: this.price,
            maxPerson: this.maxPerson
        };
    }
}

export class FestivalTypes {
    static EDUCATION = "Education";
    static MUSIC = "Music";
    static ART = "Art";
    static FOOD = "Food";
    static FILM = "Film";

    static keys() { 
        return ["EDUCATION", "MUSIC", "ART", "FOOD", "FILM"];
    } 
    static values() { 
        return ["Education", "Music", "Art", "Food", "Film"];
    }
    static entries() { 
        return [["EDUCATION", "Education"], ["MUSIC", "Music"], ["ART", "Art"], ["FOOD", "Food"], ["FILM", "Film"]];
    }
}

export class FestivalTransportations {
    static BUS = "Bus";
    static PLANE = "Plane";
    static OWN = "Own";
    static keys() { 
        return ["BUS", "PLANE", "OWN"];
    }
    static values() { 
        return ["Bus", "Plane", "Own"];
    }
    static entries() { 
        return [["BUS", "Bus"], ["PLANE", "Plane"], ["OWN", "Own"]];
    }
}