/* DECLARATIONS */
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
  mainElement.style.justifyContent = 'space-around';
  mainElement.style.alignItems = 'stretch';
  console.log(result);
  const pageTitle = document.getElementsByTagName('title')[0];
  const place = new Place(result.data);
  pageTitle.textContent = `${place.title}`;

  const title = document.createElement('h1');
  mainElement.prepend(title);
  title.textContent = place.title;
  title.style.marginTop = '40px';
  title.style.marginBottom = '20px';
  title.style.alignSelf = 'center';

  const card = document.getElementById('place-details');
  card.classList.add('sole-place-card'); // for future retrieval / CSS styling
  card.classList.add('flex-container');
  card.classList.add('vt-flex-container');
  card.classList.add('centered-flex');
  card.setAttribute('id', `${place.id}`);
  card.style.backgroundColor = '#ffffff';
  card.style.display = 'flex';
  card.style.justifyContent = 'space-between';
  card.style.paddingBlock = '40px';
  card.style.borderRadius = '10px';
  card.style.boxShadow = '0 3px 10px rgb(0 0 0 / 0.2)';
  card.style.flexGrow = '2';
  card.style.margin = '0 10px 0 10px';

  const host = document.createElement('span');
  host.innerHTML = `<b>Host:</b> ${place.owner.first_name} ${place.owner.last_name}`;
  card.appendChild(host);
  host.style.padding = '8px 0 8px 0';

  const price = document.createElement('span');
  price.innerHTML = `<b>Price per night:</b> ${place.price}$`;
  card.appendChild(price);
  price.style.padding = '8px 0 8px 0';

  const description = document.createElement('span');
  description.innerHTML = `<b>Description:</b> ${place.description}`;
  card.appendChild(description);
  description.style.padding = '8px 0 8px 0';

  const amenities = document.createElement('span');
  // reduce(function, initialAccumulatorValue)
  // reduce((result, amenity, index) => {add separator first if not first element}, iAV = '');
  const amenityNamesString = place.amenities.reduce((result, amenity, index) => {
    return result + (index > 0 ? ', ' : '') + amenity.name;
  }, '');
  amenities.innerHTML = `<b>Amenities:</b> ${amenityNamesString}`;
  card.appendChild(amenities);
  amenities.style.padding = '8px 0 8px 0';
}

function buildReviewCard(parentElement, review) {
  const card = document.createElement('article');

  card.setAttribute('id', `${review.id}`);
  card.style.margin = '20px 10px 20px 10px';
  card.style.padding = '30px';
  card.style.backgroundColor = '#ffffff';
  card.style.borderRadius = '15px';
  card.style.padding = '15px';
  card.style.alignItems = 'center';
  card.style.textAlign = 'center';
  card.style.borderRadius = '10px';
  card.style.boxShadow = '0 3px 10px rgb(0 0 0 / 0.2)';
  parentElement.appendChild(card);

  const cardContent = document.createElement('div');
  card.appendChild(cardContent);
  cardContent.style.textAlign = 'left';

  const cardTitle = document.createElement('h4');
  cardTitle.textContent = `${review.user.first_name} ${review.user.last_name}:`;
  cardContent.appendChild(cardTitle);
  cardTitle.style.padding = '8px 0 8px 0';

  const cardReview = document.createElement('p');
  cardReview.textContent = `${review.text}`;
  cardContent.appendChild(cardReview);
  cardReview.style.padding = '8px 0 8px 0';

  const cardRating = document.createElement('p');
  cardContent.appendChild(cardRating);
  cardRating.style.padding = '8px 0 8px 0';

  const ratingLabel = document.createElement('span');
  ratingLabel.textContent = "Rating: ";
  cardRating.appendChild(ratingLabel);

  const starsContainer = document.createElement('span');
  starsContainer.style.position = 'relative';
  starsContainer.style.display = 'inline-block';
  starsContainer.style.color = '#ddd';
  cardRating.appendChild(starsContainer);

  const emptyStars = document.createElement('span');
  emptyStars.textContent = "★★★★★";
  starsContainer.appendChild(emptyStars);

  const filledStars = document.createElement('span');
  filledStars.textContent = "★★★★★";
  filledStars.style.position = 'absolute';
  filledStars.style.left = '0';
  filledStars.style.top = '0';
  filledStars.style.color = '#ff9800';
  filledStars.style.overflow = 'hidden';
  filledStars.style.width = `${(review.rating / 5) * 100}%`;
  filledStars.style.whiteSpace = 'nowrap';
  starsContainer.appendChild(filledStars);
}

function displayReviews(result) {
  const mainElement = document.getElementsByTagName('main')[0];
  const refElement = document.getElementById('reviews');
  
  const divReview = document.createElement('div');
  divReview.style.display = 'flex';
  divReview.style.flexDirection = 'row';
  divReview.style.alignItems = 'center';
  divReview.style.justifyContent = 'flex-start';
  divReview.style.margin = '20px 0 10px 0';
  refElement.parentNode.insertBefore(divReview, refElement);

  const title = document.createElement('h2');
  title.textContent = 'Reviews';
  title.style.textAlign = 'left';
  title.style.alignItems = 'center';
  title.style.justifyContent = 'flex-start';
  title.style.display = 'flex';
  divReview.appendChild(title);

  const reviewButton = document.createElement('a');
  reviewButton.setAttribute('href', `add_review.html?placeId=${placeId}`);
  reviewButton.setAttribute('id', 'review-button');
  reviewButton.classList.add('button');
  reviewButton.classList.add('review-button');
  reviewButton.textContent = 'Review this place';
  reviewButton.style.marginLeft = '20px';
  reviewButton.style.alignContent = 'center';
  divReview.appendChild(reviewButton);

  const section = document.getElementById('reviews');

  for (let review of result.data.reviews) {
    buildReviewCard(section, review);
  }
  
}

//CODE
// URL = Protocol://domain/path?querystring. Isolates query string
const urlParams = new URLSearchParams(window.location.search);
const addReviewSection = document.getElementById('add-review');
const placeId = urlParams.get('placeId');
const toast = urlParams.get('toast');
let placePromise = null;
let place = null;

placePromise = fetchPlaceDetails(placeId);

if (toast === 'success') {
  showToast('Review submitted successfully!');
}

if (!token) {
  addReviewSection.style.display = 'none';
};

document.addEventListener('DOMContentLoaded', async () => {
  const placeResult = await placePromise;
  place = placeResult.data;

  displayPlace(placeResult);
  displayReviews(placeResult);

  const reviewButton = document.getElementById('review-button');

  reviewSubmitListener();

  if (token) {
    reviewButton.style.display = 'block';
  } else {
    reviewButton.style.display = 'none';
  };
});
