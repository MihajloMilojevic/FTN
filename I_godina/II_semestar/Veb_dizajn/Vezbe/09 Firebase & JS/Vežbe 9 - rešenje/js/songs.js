let firebaseUrl =
  "http://web-dizajn-a70f1-default-rtdb.europe-west1.firebasedatabase.app";

let songsUrl = firebaseUrl + "/songs.json";

let songsUl = document.getElementById("audioPlaylist");

let artistSpanElement = document.getElementById("artistElement");
let titleSpanElement = document.getElementById("titleElement");
let audioPlayer = document.getElementById("player");

let request = new XMLHttpRequest();
request.onreadystatechange = function () {
  if (this.readyState == 4) {
    if (this.status == 200) {
      // console.log(this.responseText);
      let songs = JSON.parse(this.responseText);
      console.log(songs);

      for (let i = 0; i < songs.length; i++) {
        // i=1
        let currentSong = songs[i];
        //  console.log(currentSong);
        let songLi = document.createElement("li");

        let orderNumberSpan = document.createElement("span");
        orderNumberSpan.classList.add("orderNumber");
        orderNumberSpan.innerText = i + 1;
        songLi.appendChild(orderNumberSpan);

        let artistSpan = document.createElement("span");
        artistSpan.classList.add("artistSpan");
        artistSpan.innerText = currentSong.artist;
        songLi.appendChild(artistSpan);

        let titleSpan = document.createElement("span");
        titleSpan.classList.add("songSpan");
        titleSpan.innerText = currentSong.title;
        songLi.appendChild(titleSpan);

        songLi.addEventListener("click", function (e) {
          artistSpanElement.innerText = currentSong.artist;
          titleSpanElement.innerText = currentSong.title;
          audioPlayer.setAttribute("src", currentSong.link);
          audioPlayer.play();
        });

        songsUl.appendChild(songLi);
      }
    } else {
      alert("Greska prilikom dobavljanja podataka");
    }
  }
};
request.open("GET", songsUrl);
request.send();
