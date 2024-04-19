// URL Firebase projekta - Obratiti paznju da je uklonjen znak / sa kraja!
// Obavezno postavite URL do svog Firebase projekta da bi sve radilo kako treba
let firebaseUrl =
'https://web-design-10-default-rtdb.firebaseio.com';

let cars = {}; // Objekat koji ce cuvati sve automobile sa Firebase-a

( async function () {
  await fetch("https://prvi-projekat-4b9b7-default-rtdb.europe-west1.firebasedatabase.app/test.json", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: "Test",
      age: 25,
    }),
  })
})();

// Pozivamo ucitavanje svih automobila prilikom ucitavanja stranice
getAllCars();

/*
    Funkcija koja dobavlja sve automobile i dodaje ih u tabelu
*/
function getAllCars() {
  let request = new XMLHttpRequest();

  request.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        // Brisanje prethodnog sadrzaja tabele
        removeTableRows("allCars");

        cars = JSON.parse(request.responseText);
        console.log(cars);

        // Izdvajanje svakog pojedinacnog automobila iteriranjem kroz atribute objekta
        for (let id in cars) {
          let car = cars[id];
          // console.log(car);
          appendCarRow("allCars", id, car);
        }
      } else {
        alert("Greška prilikom učitavanja svih automobila.");
      }
    }
  };

  request.open("GET", firebaseUrl + "/cars.json");
  request.send();
}

/*
    Funkcija koja otvara stranicu za izmenu
*/
function showEditPage() {
  let clickedBtn = this;
  // console.log(clickedBtn);
  let carId = clickedBtn.getAttribute("data-id");
  window.location.href = "edit.html?id=" + carId;
}

/*
    Funkcija koja briše željeni automobil
*/
function deleteCar() {
  let clickedBtn = this;
  let carId = clickedBtn.getAttribute("data-id");

  let request = new XMLHttpRequest();

  request.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        getAllCars();
      } else {
        alert("Greška prilikom brisanja automobila.");
      }
    }
  };

  request.open("DELETE", firebaseUrl + "/cars/" + carId + ".json");
  request.send();
}

// *********************************************
//               POMOCNE FUNCKIJE
// *********************************************

/* 
    Pomocna funckija koja dodaje red u tabelu
*/
function appendCarRow(tBody, id, car) {
  let carRow = document.createElement("tr");

  let brandTd = document.createElement("td");
  brandTd.innerText = car.brand;
  carRow.appendChild(brandTd);

  let modelTd = document.createElement("td");
  modelTd.innerText = car.model;
  carRow.appendChild(modelTd);

  let yearTd = document.createElement("td");
  yearTd.innerText = car.year;
  carRow.appendChild(yearTd);

  // <button type="button" onclick="showEditPage()" data-id="neki_id">Izmeni</button>
  let editBtn = document.createElement("button");
  editBtn.type = "button";
  editBtn.innerText = "Izmeni";
  editBtn.onclick = showEditPage;
  editBtn.setAttribute("data-id", id);

  let editTd = document.createElement("td");
  editTd.appendChild(editBtn);
  carRow.appendChild(editTd);

  let deleteBtn = document.createElement("button");
  deleteBtn.type = "button";
  deleteBtn.innerText = "Obriši";
  deleteBtn.onclick = deleteCar;
  deleteBtn.setAttribute("data-id", id);

  let deleteTd = document.createElement("td");
  deleteTd.appendChild(deleteBtn);
  carRow.appendChild(deleteTd);

  document.getElementById(tBody).appendChild(carRow);
}

/*
    Pomocna funkcija koja brise sve redove iz tabele
*/
function removeTableRows(tBodyId) {
  let tBody = document.getElementById(tBodyId);
  while (tBody.firstChild) {
    tBody.removeChild(tBody.lastChild);
  }
}
