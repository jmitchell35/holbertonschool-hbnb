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

function buildPlaceCard(place, parentElement) {
  // article = card container = flex vertical stack
    // image slot = img for later
    // card content = div = grid container
      // title = h3
      // description = p
      // price = p
      // view details = link / button

  const card = document.createElement('article');
  card.classList('place-card');
  card.classList('flex-container');
  card.classList('vt-flex-container');
  card.setAttrinute('id', `${place.id}`)
  parentElement.appendChild(card);

  const cardContent = document.createElement('div');
  cardContent.classList('flex-container');
  cardContent.classList('vt-flex-container');
  card.appendChild(cardContent);

  const cardTitle = document.createElement('h3');
  cardTitle.classList('placeCardTitle'); // to be defined as CSS style
  cardTitle.textContent = `${place.title}`;
  cardContent.appendChild(cardTitle);

  const cardDescription = document.createElement('p');
  cardDescription.classList('placeInfo'); // to be defined as CSS style
  cardDescription.textContent = `${place.description}`;
  cardContent.appendChild(cardDescription);

  const cardPrice = document.createElement('p');
  cardPrice.classList('placeInfo');
  cardPrice.textContent = `${place.price}$ per night`;
  cardContent.appendChild(cardPrice);

  const cardOpener = document.createElement('a');
  cardOpener.classList.add('button');
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
    buildPlaceCard(place, placesSection);
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
