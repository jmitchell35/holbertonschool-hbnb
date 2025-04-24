from app import create_app
from flask_cors import CORS

app = create_app()

CORS(app, 
     resources={r"/*": {"origins": ["http://localhost:5500", "http://127.0.0.1:5500"]}},
     supports_credentials=True,
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"])

@app.after_request
def after_request(response):
    """Ensure CORS headers are set on all responses"""
    # Allow CORS from development frontend
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/api/test', methods=['GET'])
def test_endpoint():
    """Simple endpoint to test API is working"""
    return jsonify({"status": "success", "message": "API is working"})

if __name__ == '__main__':
    app.run()
