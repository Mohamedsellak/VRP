var map = L.map('map').setView([34.032249720296896, -4.994637966156007], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

locations = []


// Define the new marker icon
var newIcon = L.icon({
    iconUrl: 'assets/images/icon.png',
    iconSize: [32, 32]
});


// Add a click event listener to the marker
function onMarkerClick(e) {
    map.removeLayer(e.target);
    locations.splice(locations.indexOf(e.target.getLatLng()), 1);
}

// dealing with clicks in map
function onMapClick(e) {
    if (locations.length == 0) {
        var marker = L.marker(e.latlng, { icon: newIcon }).addTo(map);
    } else {
        var marker = L.marker(e.latlng).addTo(map);
    }
        locations.push(e.latlng)
        marker.on('click', onMarkerClick);
}
map.on('click', onMapClick);


// function to draw a route between locations
function drawRoute(locations) {
    L.Routing.control({
        waypoints: locations,
        showAlternatives: false, // hide alternative routes
        routeWhileDragging: false,
        optimizedWaypoints: false,
        router: L.Routing.osrmv1({
            serviceUrl: 'https://router.project-osrm.org/route/v1',
            profile: 'driving'
        }),
        createMarker: function(i, waypoint, n) {
            const marker = L.marker(waypoint.latLng).addTo(map);
            marker.bindTooltip(`Location ${i}`, { permanent: true, direction: 'top' }).openTooltip();
            return marker;
        }
    }).addTo(map);
}


// the validation button
const button = document.querySelector('.btn');
button.addEventListener('click', () => {
    // send the data to the server
    fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "locations": locations })
    })
    .then(response => response.json())

    // draw route between locations
    .then(data => drawRoute(data) )
});