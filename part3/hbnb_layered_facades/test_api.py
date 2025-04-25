import requests

def test_api():
    """Test the login API endpoint directly with requests"""
    url = "http://127.0.0.1:5000/api/v1/login"
    
    # Test credentials - modify as needed
    payload = {
        "email": "admin@gmail.com", 
        "password": "12345"  # Update with the correct password
    }

    print(f"Testing POST to {url} with payload: {payload}")

    try:
        # First test the OPTIONS request
        options_response = requests.options(
            url, 
            headers={
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type"
            }
        )
        print(f"OPTIONS Response Status: {options_response.status_code}")
        print(f"OPTIONS Response Headers: {dict(options_response.headers)}")
        
        # Now test the actual POST request
        response = requests.post(url, json=payload)
        
        print(f"POST Response Status: {response.status_code}")
        print(f"POST Response Headers: {dict(response.headers)}")
        
        # Try to parse as JSON
        try:
            json_data = response.json()
            print(f"JSON Response: {json_data}")
        except ValueError:
            # If not JSON, print the text (first 500 chars)
            print(f"Not a JSON response. Text (first 500 chars): {response.text[:500]}")
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    test_api()
