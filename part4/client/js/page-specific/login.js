document.addEventListener('DOMContentLoaded', () => {
  mainIsFlex();
  const loginForm = document.getElementById('login-form');

  loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const response = await fetch('http://127.0.0.1:5000/api/v1/login', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: `${loginForm.email.value}`,
                password: `${loginForm.password.value}`}),
        })

        if (response.ok) {
            const data = await response.json();

            document.cookie = `token=${data.access_token}; path=/`;

            window.location.href = 'index.html';
        } else {
            alert('Login failed: ' + response.statusText);
        }
    });
});
