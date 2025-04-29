/* DECLARATIONS */
async function fetchPlaceDetails(token, placeId) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP request to API failed. Status : ${response.status}`)
    };

    const placeResponse = await response.json();
    return { success: true, data: placeResponse };

  } catch (error) {
    console.error('Error fetching places:', error);
    return { success: false, error: error.message };
  }
}

class Place {
  constructor(data) {
    this.id = data.id;
    this.title = data.title;
    this.description=data.description;
    this.price=data.price;
    this.amenities=data.amenities;
    this.latitude=data.latitude;
    this.longitude=data.longitude;
    this.owner= data.owner;
    this.reviews=data.reviews;
  }
}

function displayPlace(result) {
  const mainElement = mainIsFlex();
  console.log(result);
  const pageTitle = document.getElementsByTagName('title')[0];
  const place = new Place(result.data);
  pageTitle.textContent = `${place.title}`;

  const title = document.createElement('h1');
  mainElement.prepend(title);
  title.textContent = place.title;

  const card = document.getElementById('place-details');
  card.classList.add('sole-place-card'); // for future retrieval / CSS styling
  card.classList.add('flex-container');
  card.classList.add('vt-flex-container');
  card.classList.add('centered-flex');
  card.setAttribute('id', `${place.id}`);

  const host = document.createElement('span');
  host.innerHTML = `<b>Host:</b> ${place.owner.first_name} ${place.owner.last_name}`;
  card.appendChild(host);

  const price = document.createElement('span');
  price.innerHTML = `<b>Price per night:</b> ${place.price}$`;
  card.appendChild(price);

  const description = document.createElement('span');
  description.innerHTML = `<b>Description:</b> ${place.description}`;
  card.appendChild(description);

  const amenities = document.createElement('span');
  amenities.innerHTML = `<b>Amenities:</b> ${place.amenities}`;
  card.appendChild(amenities);


}
// URL = Protocol://domain/path?querystring. Isolates query string
const urlParams = new URLSearchParams(window.location.search);
const addReviewSection = document.getElementById('add-review');
const placeId = urlParams.get('placeId');
let placePromise = null;
let place = null;

if (token) {
  addReviewSection.style.display = 'block';
  placePromise = fetchPlaceDetails(token, placeId);
} else {
  addReviewSection.style.display = 'none';
};

document.addEventListener('DOMContentLoaded', async () => {
  const placeResult = await placePromise;
  let place = placeResult.data;
  displayPlace(placeResult);
});
