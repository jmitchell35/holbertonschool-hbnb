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

function buildPlaceCard(data, parentElement) {
  let place = new Place(data)
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

  const cardTitle = document.createElement('h4');
  cardTitle.classList.add('placeCardTitle'); // to be defined as CSS style
  cardTitle.textContent = `${place.title}`;
  cardContent.appendChild(cardTitle);

  const cardDescription = document.createElement('p');
  cardDescription.classList.add('place-info'); // to be defined as CSS style
  cardDescription.textContent = `${place.description}`;
  cardContent.appendChild(cardDescription);

  const cardPrice = document.createElement('p');
  cardPrice.classList.add('place-info');
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
  placesElements.push({
    card,
    data,
  });

  return card
}

function populatePlaces(placesData) {
  for (let place of placesData) {
    buildPlaceCard(place, placesSection);
  };
}

function calculateQuartiles(values) {
  if (values.length === 0) {
    throw new Error('Input array is empty');
  }

  // Create a sorted copy of the array
  const sorted = [...values].sort((a, b) => a - b);
  const n = sorted.length;

  // Calculate indices
  const q1Index = Math.floor(n / 4);
  const medianIndex = Math.floor(n / 2);
  const q3Index = Math.floor(n * 3 / 4);

  // Calculate median (Q2)
  let median;
  if (n % 2 === 0) { // Even length
    median = (sorted[medianIndex - 1] + sorted[medianIndex]) / 2;
  } else { // Odd length
    median = sorted[medianIndex];
  }
  median = Math.floor(median + 1)

  // Calculate Q1
  let q1;
  if (n % 4 === 0) { // If n is divisible by 4, average two values
    q1 = (sorted[q1Index - 1] + sorted[q1Index]) / 2;
  } else {
    q1 = sorted[q1Index];
  }
  q1 = Math.floor(q1 + 1)

  // Calculate Q3
  let q3;
  if (n % 4 === 0) { // If n is divisible by 4, average two values
    q3 = (sorted[q3Index - 1] + sorted[q3Index]) / 2;
  } else {
    q3 = sorted[q3Index];
  }
  q3 = Math.floor(q3 + 1)

  return { q1, median, q3 };
}

function setDynamicFilterValues(placesElements) {
  let pricesList = [];
  for (let place of placesElements) {
    pricesList.push(place.data.price);
  };

  return calculateQuartiles(pricesList);
}

function populateFilter(placesElements) {
  const priceFilter = document.getElementById('price-filter');
  const filter1 = document.createElement('option');
  const filter2 = document.createElement('option');
  const filter3 = document.createElement('option');
  const filter4 = document.createElement('option');
  filter4.setAttribute('value', 'All');
  filter4.setAttribute('selected', 'selected');
  filter4.textContent= 'All';

  priceFilter.appendChild(filter1);
  priceFilter.appendChild(filter2);
  priceFilter.appendChild(filter3);
  priceFilter.appendChild(filter4);

  if (placesElements.length > 0) {
    const filters = setDynamicFilterValues(placesElements);
    filter1.setAttribute('value', filters.q1);
    filter1.textContent= `${filters.q1}`;
    filter2.setAttribute('value', filters.median);
    filter2.textContent= `${filters.median}`;
    filter3.setAttribute('value', filters.q3);
    filter3.textContent= `${filters.q3}`;
  } else {
    filter1.setAttribute('value', 10);
    filter1.textContent= '10';
    filter2.setAttribute('value', 50);
    filter2.textContent= '50';
    filter3.setAttribute('value', 100);
    filter3.textContent= '100';
  }
}

// CODE
const placesSection = document.getElementById('places-list');
let placesPromise = null;
let placesElements = [];

if (token) {
  placesPromise = fetchPlaces(token);
};

document.addEventListener('DOMContentLoaded', async () => {
  const result = await placesPromise;
  const filter = document.getElementById('price-filter');

  if (result.success) {
    populatePlaces(result.data);
    populateFilter(placesElements);
  } else {
    populateFilter([]);
    placesSection.textcontent = `${result.error}`;
  };

  filter.addEventListener('change', (event) => {
    const selected = event.target.value;
    for (placeElement of placesElements) {
      let place = new Place(placeElement.data);
      if (place.price > selected) {
        placeElement.card.style.display = 'none';
      } else {
        placeElement.card.style.display = 'block';
      };
    };
  });
});
