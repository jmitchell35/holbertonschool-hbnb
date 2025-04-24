document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    
    // Add a status message element
    const statusDiv = document.createElement('div');
    statusDiv.id = 'login-status';
    statusDiv.style.marginTop = '15px';
    statusDiv.style.padding = '10px';
    statusDiv.style.borderRadius = '5px';
    statusDiv.style.display = 'none';
    loginForm.appendChild(statusDiv);
    
    function showStatus(message, isError = false) {
      statusDiv.textContent = message;
      statusDiv.style.display = 'block';
      statusDiv.style.backgroundColor = isError ? '#ffebee' : '#e8f5e9';
      statusDiv.style.color = isError ? '#c62828' : '#2e7d32';
    }
    
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      
      try {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
  
        showStatus('Attempting to login...');
        console.log('Attempting login with:', { email });
  
        const apiUrl = 'http://127.0.0.1:5000/api/v1/auth/login';
        console.log('API URL:', apiUrl);
        
        // First try an OPTIONS request to see if CORS is working
        try {
          console.log('Testing CORS with OPTIONS request...');
          const optionsResponse = await fetch(apiUrl, {
            method: 'OPTIONS',
            headers: {
              'Access-Control-Request-Method': 'POST',
              'Access-Control-Request-Headers': 'Content-Type'
            }
          });
          console.log('OPTIONS response status:', optionsResponse.status);
        } catch (optionsError) {
          console.error('OPTIONS request failed:', optionsError);
        }
        
        // Now try the actual POST request
        const response = await fetch(apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
        });
        
        console.log('Response status:', response.status);
        console.log('Response headers:', Object.fromEntries(response.headers.entries()));
        
        // Get the raw text first to debug
        const responseText = await response.text();
        console.log('Raw response:', responseText);
        
        // If it's not valid JSON, show the error
        if (!response.ok) {
          // Try to parse JSON, but if it fails, use the raw text
          let errorMessage;
          try {
            const errorData = JSON.parse(responseText);
            errorMessage = errorData.error || `Server returned ${response.status}`;
          } catch (jsonError) {
            // If it's not JSON, it might be HTML or plain text
            errorMessage = `Server returned ${response.status}: Not a valid JSON response`;
            // Show part of the response for debugging
            if (responseText.length > 0) {
              errorMessage += ` - First 100 chars: ${responseText.substring(0, 100)}...`;
            }
          }
          throw new Error(errorMessage);
        }
        
        // If we got this far, try to parse the JSON
        const data = JSON.parse(responseText);
        console.log('Login successful, token received');
        showStatus('Login successful! Redirecting...');
  
        localStorage.setItem('accessToken', data.access_token);
        
        // Redirect after a short delay
        setTimeout(() => {
          window.location.href = 'index.html';
        }, 1500);
  
      } catch (error) {
        console.error('Login error:', error);
        showStatus(`Login failed: ${error.message}`, true);
      }
    });
  });
  