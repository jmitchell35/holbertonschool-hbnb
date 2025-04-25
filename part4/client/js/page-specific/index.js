// DECLARATIONS
function getCookie(name) {
  // Function to get a cookie value by its name
  const cookie = document.cookie // string where key=value are separated by "; " + method chaining
  .split("; ")
  .find(cookie => cookie.startsWith(`${name}=`))
  ?.split("=")[1];

  return cookie;
}

async function fetchPlaces(token) {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      }
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

// CODE
const token = getCookie('token');
const loginLink = document.getElementById('login-link');
let placesPromise = null;

if (token) {
  placesPromise = fetchPlaces(token);
  loginLink.style.display = 'none';
};

document.addEventListener('DOMContentLoaded', async () => {
  const result = await placesPromise;
  console.log(result);
});
