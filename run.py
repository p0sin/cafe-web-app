# Import the create_app function from the website module
from app import create_app

# Create the Flask application using the create_app function
flask_app = create_app()

# Check if this script is being run directly
if __name__ == '__main__':
    # Run the Flask application in debug mode
    flask_app.run(host='0.0.0.0', debug=True)
