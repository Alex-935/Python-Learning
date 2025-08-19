# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def home():
    # Function that handles requests to the root URL
    return "Hello, World!"


#You are all set to run the server. Use the following command to run the server from the terminal:
#flask --app server --debug run


#curl -X GET -i -w '\n' localhost:5000
#The -X argument specifies the GET command, and the -i argument displays the header from the response.
#You should see Hello World returned as the output of the CURL command. Note the return status of HTTP 200 OK and the Content-type of text/html.


#returning JSON

# Import the Flask class from the flask module
from flask import Flask, jsonify
# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)
# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Create a dictionary to return as a response
    return {"message": "Hello World"}

#curl -X GET -i -w '\n' localhost:5000