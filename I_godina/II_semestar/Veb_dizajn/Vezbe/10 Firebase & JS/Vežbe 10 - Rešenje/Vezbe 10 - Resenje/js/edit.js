// URL Firebase projekta - Obratiti paznju da je uklonjen znak / sa kraja!
// Obavezno postavite URL do svog Firebase projekta da bi sve radilo kako treba
let firebaseUrl =
"https://web-design-10-default-rtdb.firebaseio.com";

let carId = getParamValue("id");
let car = {};

/* 
    Dobavljanje automobila po id-ju prilikom ucitavanja stranice 
*/
let getRequest = new XMLHttpRequest();

getRequest.onreadystatechange = function (e) {
  if (this.readyState == 4) {
    if (this.status == 200) {
      car = JSON.parse(getRequest.responseText);
      document.getElementById("brand").value = car.brand;
      document.getElementById("model").value = car.model;
      document.getElementById("year").value = car.year;
      console.log(car);
    } else {
      alert("Greška prilikom učitavanja automobila.");
    }
  }
};

getRequest.open("GET", firebaseUrl + "/cars/" + carId + ".json");
getRequest.send();

/* 
    Izmena automobila na 'submit' forme 
*/
let editForm = document.getElementById("editForm");
// Na izmenu cemo reagovati tako sto uhvatimo 'submit' dogadjaj na editForm
editForm.addEventListener("submit", function (e) {
  // Sprecicemo slanje forme na server, jer zelimo mi da imamo kontrolu nad time
  e.preventDefault();

  let brand = document.querySelector("#brand").value.trim();
  let model = document.querySelector("#model").value.trim();
  let year = document.querySelector("#year").valueAsNumber;

  /* Drugi nacin:
        let yearText = document.getElementById('year').value;
        let year = parseInt(yearText);
    */

  /* Bolje resenje: ne dozvoliti slanje ukoliko je bilo koji podatak nevalidan,
   i u tom slucaju obavestiti korisnika */
  if (brand != "") {
    car.brand = brand;
  }
  if (model != "") {
    car.model = model;
  }
  if (!isNaN(year)) {
    // Isto sto i: if (isNaN(year) == false)
    car.year = year;
  }
  // console.log(car);

  let putRequest = new XMLHttpRequest();

  putRequest.onreadystatechange = function (e) {
    if (this.readyState == 4) {
      if (this.status == 200) {
        window.location.href = "index.html";
      } else {
        alert("Greška prilikom izmene automobila.");
      }
    }
  };

  putRequest.open("PUT", firebaseUrl + "/cars/" + carId + ".json");
  putRequest.send(JSON.stringify(car));
});

/* 
    Pomocna funkcija koja ocitava vrednost URL parametra sa prosledjenim imenom
 */
function getParamValue(name) {
  let location = decodeURI(window.location.toString());
  let index = location.indexOf("?") + 1;
  let subs = location.substring(index, location.length);
  let splitted = subs.split("&");

  for (i = 0; i < splitted.length; i++) {
    let s = splitted[i].split("=");
    let pName = s[0];
    let pValue = s[1];
    if (pName == name) {
      return pValue;
    }
  }
}
