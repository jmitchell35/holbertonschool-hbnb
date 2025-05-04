// Setting up main header and footer
// DECLARATION
function setUpHeader() {
  const bodyElement = document.getElementsByTagName('body')[0];
  bodyElement.classList.add('flex-container');
  bodyElement.classList.add('vt-flex-container');

  const headerElement = document.createElement('header');
  headerElement.classList.add('flex-container');
  headerElement.classList.add('vt-flex-container');

  const divElement = document.createElement('div');
  divElement.setAttribute('id', 'main-nav-bar-layout-div');
  divElement.classList.add('flex-container');
  divElement.classList.add('hz-flex-container');
  divElement.classList.add('top-header');


  const headerLoginNavElement = document.createElement('nav');
  headerLoginNavElement.classList.add('flex-container');
  headerLoginNavElement.classList.add('vt-flex-container');
  headerLoginNavElement.classList.add('header-nav');
  headerElement.appendChild(divElement);

  const headerLogoElement = document.createElement('img');
  headerLogoElement.setAttribute('src', '../resources/images/logo.png');
  headerLogoElement.setAttribute('alt', 'hbnb-logo');
  headerLogoElement.setAttribute('title', 'hbnb-logo');
  divElement.appendChild(headerLogoElement);

  const loginLinkElement = document.createElement('a');
  loginLinkElement.setAttribute('href', 'login.html');
  loginLinkElement.setAttribute('id', 'login-link');
  loginLinkElement.classList.add('login-button');
  loginLinkElement.classList.add('button');
  loginLinkElement.textContent = 'Login';
  headerLoginNavElement.appendChild(loginLinkElement);
  divElement.appendChild(headerLoginNavElement);

  document.querySelector('body').prepend(headerElement);

  //setUpNavBar();
}

function mainIsFlex() {
  const mainElement = document.getElementsByTagName('main')[0];
  mainElement.classList.add('flex-container');
  mainElement.classList.add('vt-flex-container');
  mainElement.classList.add('centered-flex');

  return mainElement;
}

function setUpFooter() {
  const footerElement = document.createElement('footer');
  footerElement.classList.add('flex-container');
  footerElement.classList.add('hz-flex-container');
  footerElement.classList.add('centered-flex');
  
  const spanFooterElement = document.createElement('span');
  spanFooterElement.textContent = '© 2024 HBnB Evolution - all rights reserved';

  footerElement.appendChild(spanFooterElement);
  document.querySelector('body').appendChild(footerElement);
}

function setUpNavBar() {
  const navBarElement = document.createElement('nav');
  navBarElement.setAttribute('id', 'main-nav-bar');
  navBarElement.classList.add('flex-container');
  navBarElement.classList.add('hz-flex-container');
  
  const navArray = ['index'];
  const displayArray = ['Home'];
  const titleArray = ['Home page'];
  for (let navButton of navArray) {
    let itemIndex = navArray.indexOf(`${navButton}`);
    let navElement = document.createElement('a');
    navElement.setAttribute('href', `${navButton}.html`);
    navElement.setAttribute('title', `${titleArray[itemIndex]}`);
    navElement.textContent = `${displayArray[itemIndex]}`;
    navBarElement.appendChild(navElement);
  };

  document.querySelector('header').appendChild(navBarElement);
}

function getCookie(name) {
  // Function to get a cookie value by its name
  const cookie = document.cookie // string where key=value are separated by "; " + method chaining
  .split('; ')
  .find(string => string.startsWith(`${name}=`))
  ?.split('=')[1];

  return cookie;
}

// Make main flexible on every page for consistency
function setupMainForFlexibility() {
  const mainElement = document.getElementsByTagName('main')[0];
  if (mainElement) {
    // We don't overwrite existing classes, just add if not present
    if (!mainElement.classList.contains('flex-container')) {
      mainElement.classList.add('flex-container');
    }
    if (!mainElement.classList.contains('vt-flex-container')) {
      mainElement.classList.add('vt-flex-container');
    }
  }

  return mainElement;
}

function setUpFavicon() {
  const head = document.getElementsByTagName('head')[0];
  const favicon = document.createElement('link');
  favicon.setAttribute('rel', 'icon');
  favicon.setAttribute('href', '../resources/images/icon.png');
  favicon.setAttribute('type', 'image/png');
  head.appendChild(favicon);
}

async function fetchPlaceDetails(placeId) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
      method: 'GET'
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

function reloadStylesheets() {
  const links = document.getElementsByTagName("link");
  for (let i = 0; i < links.length; i++) {
    const link = links[i];
    if (link.rel === "stylesheet") {
      link.href = link.href.split("?")[0] + "?reload=" + new Date().getTime();
    }
  }
}

function adaptReviewForm() {
  const form = document.getElementById('review-form');
  if (form) {
    const text = form.getElementsByTagName('textarea')[0];
    text.setAttribute('placeholder', 'Tell us about your stay...')

  };

  const select = document.getElementById('rating');

  if (select) {
    const rating = document.createElement('input');
    select.replaceWith(rating);
    rating.setAttribute('type', 'range');
    rating.setAttribute('min', '1');
    rating.setAttribute('max', '5');
    rating.setAttribute('value', '2');
  };

  return form;
}

function showToast(message, type = 'success') {
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = message;
  document.body.appendChild(toast);
  
  // Animation
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 500);
  }, 5000);
}

function reviewSubmitListener() {
  reviewForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const selectedRating = document.querySelector('input[name="rating"]:checked');
    if (!selectedRating) {
      alert('Please select a rating');
      return;
    }

    const value = parseInt(selectedRating.value, 10);
    console.log(value);

    const response = await fetch('http://127.0.0.1:5000/api/v1/reviews', {
      method: 'POST',
      headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
      },
      body: JSON.stringify({
          text: document.getElementById('review-text').value,
          rating: value,
          place_id: placeId,
      }),
    });

    if (response.ok) {
      document.getElementById('review-text').value = '';
      document.querySelectorAll('input[name="rating"]:checked')
        .forEach(input => input.checked = false);
        showToast('Review submitted successfully !');
      window.location.href = `place.html?placeId=${placeId}`;
    } else {
          alert('Review submission failed: ' + response.statusText);
    }
  });
}

// CODE STARTS HERE
setUpFavicon();
setUpHeader();
setUpFooter();
const mainElement = setupMainForFlexibility();
const loginLink = document.getElementById('login-link');
const token = getCookie('token');
console.log(token);
let reviewForm = null;

if (token) {
  loginLink.style.display = 'none';
} else {
  loginLink.style.display = 'block';
};

document.addEventListener('DOMContentLoaded', () => {
  setupMainForFlexibility();
  reviewForm = adaptReviewForm();
  });
