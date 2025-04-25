// Setting up main header and footer
// DECLARATION
function setUpHeader() {
  const headerElement = document.createElement('header');
  headerElement.classList.add('flex-container');
  headerElement.classList.add('vt-flex-container');
  


  const divElement = document.createElement('div');
  divElement.setAttribute('id', 'main-nav-bar-layout-div');
  divElement.classList.add('flex-container');
  divElement.classList.add('hz-flex-container');
  divElement.classList.add('top-header');


  const headerLoginNavElement = document.createElement('nav');

  const headerLogoElement = document.createElement('img');
  headerLogoElement.setAttribute('src', '../resources/images/logo.png');
  headerLogoElement.setAttribute('alt', 'hbnb-logo');
  headerLogoElement.setAttribute('title', 'hbnb-logo');
  divElement.appendChild(headerLogoElement);

  const loginLinkElement = document.createElement('a');
  loginLinkElement.setAttribute('href', 'login.html');
  loginLinkElement.setAttribute('id', 'login-link');
  loginLinkElement.classList.add('login-button');
  loginLinkElement.textContent = 'Login';
  headerLoginNavElement.appendChild(loginLinkElement);
  divElement.appendChild(headerLoginNavElement);

  headerElement.appendChild(divElement);

  document.querySelector('body').prepend(headerElement);

  setUpNavBar();
}

function setUpFooter() {
  const footerElement = document.createElement('footer');
  footerElement.classList.add('flex-container');
  footerElement.classList.add('hz-flex-container');
  footerElement.classList.add('centered-flex-single-item');
  
  const spanFooterElement = document.createElement('span');

  spanFooterElement.textContent = 'all rights reserved';

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

// CODE STARTS HERE
setUpHeader();
setUpFooter();
const token = getCookie('token');
console.log(token);

document.addEventListener('DOMContentLoaded', () => {
  
  });
