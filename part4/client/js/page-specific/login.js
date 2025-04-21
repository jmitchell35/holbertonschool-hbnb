


document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
          event.preventDefault();
          // Your code to handle form submission
      });
  }
});

const form = document.getElementById('myForm');

form.addEventListener('submit', function(event) {
    // Prevent the default form submission
    event.preventDefault();
    
    // Get form data
    const formData = new FormData(form);
    
    // Do something with the data
    // For example, log all form values:
    for (const [key, value] of formData.entries()) {
        console.log(`${key}: ${value}`);
    }
    
    // You could send the data to a server, update the UI, etc.
});