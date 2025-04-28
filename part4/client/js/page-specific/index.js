// DECLARATIONS
async function fetchPlaces(token) {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP request to API failed. Status : ${response.status}`)
    };

    const placesList = await response.json();
    return { success: true, data: placesList };

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
  }
}

function buildPlaceCard(place, parentElement) {
  const card = document.createElement('article');
  card.classList.add('place-card'); // for future retrieval / CSS styling
  card.classList.add('flex-container');
  card.classList.add('vt-flex-container');
  card.setAttribute('id', `${place.id}`);
  parentElement.appendChild(card);

  const cardContent = document.createElement('div');
  cardContent.classList.add('flex-container');
  cardContent.classList.add('vt-flex-container');
  card.appendChild(cardContent);

  const cardTitle = document.createElement('h3');
  cardTitle.classList.add('placeCardTitle'); // to be defined as CSS style
  cardTitle.textContent = `${place.title}`;
  cardContent.appendChild(cardTitle);

  const cardDescription = document.createElement('p');
  cardDescription.classList.add('placeInfo'); // to be defined as CSS style
  cardDescription.textContent = `${place.description}`;
  cardContent.appendChild(cardDescription);

  const cardPrice = document.createElement('p');
  cardPrice.classList.add('placeInfo');
  cardPrice.textContent = `${place.price}$ per night`;
  cardContent.appendChild(cardPrice);

  const cardOpener = document.createElement('a');
  cardOpener.classList.add('button');
  cardOpener.classList.add('view-details');
  cardOpener.textContent = 'View Details';
  cardOpener.addEventListener('click', function(e) {
    window.location.href = `place.html?placeId=${place.id}`;
  });
  cardContent.appendChild(cardOpener);

  return card
}

function populatePlaces(placesData) {
  const placesSection = document.getElementById('places-list');
  for (let place of placesData) {
    placeObject = new Place(place);
    buildPlaceCard(placeObject, placesSection);
  };
}

// CODE
const loginLink = document.getElementById('login-link');
let placesPromise = null;

if (token) {
  placesPromise = fetchPlaces(token);
  loginLink.style.display = 'none';
};

document.addEventListener('DOMContentLoaded', async () => {
  const result = await placesPromise;
  console.log(result);

  if (result.success) {
    populatePlaces(result.data);
  } else {
    placesSection.textcontent = `${result.error}`;
  };
});
