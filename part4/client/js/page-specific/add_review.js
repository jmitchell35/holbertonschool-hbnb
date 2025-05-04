// DECLARATION

// CODE

const urlParams = new URLSearchParams(window.location.search);
const placeId = urlParams.get('placeId');
let placePromise = null;

placePromise = fetchPlaceDetails(placeId);

if (!token) {
  window.location.href = 'index.html';
}

document.addEventListener('DOMContentLoaded', async () => {
  let title = document.getElementsByTagName('h2')[0];
  const placeResult = await placePromise;
  title.textContent = `Add a review to the place "${placeResult.data.title}"`;

  mainElement.style.justifyContent = 'center';
  mainElement.style.alignItems = 'center';

  reviewSubmitListener();
});
