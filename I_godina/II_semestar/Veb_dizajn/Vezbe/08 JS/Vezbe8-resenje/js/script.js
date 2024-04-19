let photosURL = "https://jsonplaceholder.typicode.com/photos";

let currentImg;
let contentDiv = document.getElementById("content");
let overlayDiv = document.getElementById("overlay");
let imagePlaceholder = document.getElementById("imagePlaceholder");
let titlePlaceholder = document.getElementById("titlePlaceholder");
let leftArrow = document.getElementById("leftArrow");
let rightArrow = document.getElementById("rightArrow");

let request = new XMLHttpRequest();
request.onreadystatechange = function () {
  if (this.readyState == 4) {
    if (this.status == 200) {
      let photos = JSON.parse(this.responseText);

      for (let i = 0; i < 100; i++) {
        let photo = photos[i];
        createNewDiv(photo);
      }
    } else {
      alert("Greska: " + this.status);
    }
  }
};
request.open("GET", photosURL);
request.send();

overlayDiv.addEventListener("click", function (e) {
  e.stopPropagation();
});

document.body.addEventListener("click", function (e) {
  if (overlayDiv.style.display == "block") {
    overlayDiv.style.display = "none";
  }
});

leftArrow.addEventListener("click", function (e) {
  setNextElement("left");
});

rightArrow.addEventListener("click", function (e) {
  setNextElement("right");
});

function createNewDiv(photo) {
  let photoDiv = document.createElement("div");
  photoDiv.classList.add("previewDiv");
  photoDiv.style.backgroundImage = "url('" + photo.thumbnailUrl + "')";
  photoDiv.setAttribute("data-url", photo.url);
  photoDiv.setAttribute("data-title", photo.title);
  photoDiv.addEventListener("click", function (e) {
    e.stopPropagation();
    currentImg = photoDiv;
    overlayDiv.style.display = "block";
    imagePlaceholder.setAttribute("src", photo.url);
    imagePlaceholder.setAttribute("title", photo.title);
    titlePlaceholder.innerText = photo.title;
  });
  contentDiv.appendChild(photoDiv);
}

function setNextElement(direction) {
  let nextElement;
  if (direction == "right") {
    nextElement = currentImg.nextElementSibling;
  } else {
    nextElement = currentImg.previousElementSibling;
  }

  if (nextElement != null) {
    let newTitle = nextElement.getAttribute("data-title");
    let newUrl = nextElement.getAttribute("data-url");
    imagePlaceholder.setAttribute("src", newUrl);
    imagePlaceholder.setAttribute("title", newTitle);
    titlePlaceholder.innerText = newTitle;

    currentImg = nextElement;
  }
}
