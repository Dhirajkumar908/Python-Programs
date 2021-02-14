//api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
//22288cf5d0ec41d546de22ab93b44eca
const weatherApi = {
    key: "22288cf5d0ec41d546de22ab93b44eca",
    baseUrl: `https://api.openweathermap.org/data/2.5/weather?q`
}
const searchInputBox = document.getElementById('input-box');

//evant linstener function on keyprees
searchInputBox = addEventListener('keypress', (event) => {

    if (event.keyCode == 13) {
        console.log(searchInputBox.value);
        getWeatherRepoet(searchInputBox.value);
    }
});


//get weather report
function getWeatherRepoet(city) {
    fetch('${weatherApi.baseUrl}?q=${city}$appid=${weatherApi.key}$units=matric')
        .then(weather => {
            return weather.json();
        }).then(showWeatherReaport);
}




//show weather raport
function showWeatherReaport(weather) {
    console.log(weather);

}
// data maning