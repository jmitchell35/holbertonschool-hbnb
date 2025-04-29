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
    return { success: true, data: place };

  } catch (error) {
    console.error('Error fetching places:', error);
    return { success: false, error: error.message };
  }
}

function displayPlace(result) {

}
// URL = Protocol://domain/path?querystring. Isolates query string
const urlParams = new URLSearchParams(window.location.search);
const addReviewSection = document.getElementById('add-review');
const placeId = urlParams.get('placeId');
let placePromise = null;

if (token) {
  addReviewSection.style.display = 'block';
  placePromise = fetchPlaceDetails(token, placeId);
} else {
  addReviewSection.style.display = 'none';
};

document.addEventListener('DOMContentLoaded', async () => {
  const placeResult = await placePromise;
  console.log(placeResult);
  displayPlace(placeResult);
});
