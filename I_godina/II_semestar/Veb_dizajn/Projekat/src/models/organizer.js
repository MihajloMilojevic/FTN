export default class Organizer {
    constructor(id, name, address, yearOfEstablishment, logo, contactPhone, email, festivals, festivalsId) {
        this.id = id;
        this.name = name;
        this.address = address;
        this.yearOfEstablishment = yearOfEstablishment;
        this.logo = logo;
        this.contactPhone = contactPhone;
        this.email = email;
        this.festivals = festivals;
        this.festivalsId = festivalsId;
    }
    toDb() {
        return {
            name: this.name,
            address: this.address,
            yearOfEstablishment: this.yearOfEstablishment,
            logo: this.logo,
            contactPhone: this.contactPhone,
            email: this.email,
            festivals: this.festivalsId
        };
    }
}