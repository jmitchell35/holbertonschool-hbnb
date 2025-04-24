from app import create_app

app = create_app()

@app.route('/api/v1/auth/login', methods=['OPTIONS'])
def handle_login_options():
    # Create a response object
    response = app.make_default_options_response()
    
    # Add all necessary CORS headers
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    
    return response

if __name__ == '__main__':
    app.run()
