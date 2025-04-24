document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      try {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        console.log('Attempting login with:', { email });

        const response = await fetch('http://localhost:5000//api/v1/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || `Server returned ${response.status}`);
        }

        const data = await response.json();
        console.log('Login successful, token received');

        localStorage.setItem('accessToken', data.access_token);

        window.location.href = 'index.html';

    } catch (error) {
        console.error('Login error:', error);
        alert('Login failed: ' + error.message);
    }
    });
});
