// API key koji se dobija od OpenWeatherMap
var apiKey = "3726fe9cef4ab9d506ee77d8d8f7f3d1";

var currentWeatherURL = 'http://api.openweathermap.org/data/2.5/weather?units=metric&appid=' + apiKey;

var iconURL = 'http://openweathermap.org/img/w/';

var resultsContainer = document.getElementById('resultsContainer');
var searchForm = document.getElementById('searchForm');
var locationInput = document.getElementById('txtLocation');
var locationInfo = document.getElementById('locationInfo');
var conditionsInfo = document.getElementById('conditionsInfo');
var currentWeatherTbody = document.getElementById('currentWeatherTbody');

resultsContainer.style.display = 'none';

searchForm.addEventListener('submit', function (e) {
    e.preventDefault();

    var location = locationInput.value.trim();
    if (location == '') {
        alert('Morate uneti lokaciju da biste za nju dobili prognozu');
    } else {
        var request1 = new XMLHttpRequest();

        request1.onreadystatechange = function () {
            if (this.readyState == 4) {
                if (this.status == 200) {
                    var response1 = JSON.parse(request1.responseText);
                    // console.log(response1);

                    var locationName = response1.name;
                    var temp = response1.main.temp;
                    locationInfo.innerHTML = locationName + '&nbsp;&nbsp;' + temp.toFixed(0) + ' &#8451;';

                    var conditions = response1.weather[0].main;
                    conditionsInfo.innerText = conditions;

                    var icon = response1.weather[0].icon;
                    var conditionImg = document.createElement('img');
                    conditionImg.setAttribute('src', iconURL + icon + '.png');
                    conditionsInfo.appendChild(conditionImg);

                    var newRow =
                        '<tr>' +
                        '<td>' + response1.main.temp_min.toFixed(1) + ' &#8451;</td>' +
                        '<td>' + response1.main.temp_max.toFixed(1) + ' &#8451;</td>' +
                        '<td>' + response1.main.pressure + ' hPa</td>' +
                        '<td>' + response1.main.humidity + ' %</td>' +
                        '<td>' + response1.wind.speed + ' m/s</td>' +
                        '</tr>';
                    currentWeatherTbody.innerHTML = newRow;

                    resultsContainer.style.display = 'block';
                }
            }
        }

        request1.open('GET', currentWeatherURL + '&q=' + location);
        request1.send();
    }

});