# Import the necessary libraries
from flask import Flask, request, jsonify
import random


# Create a Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    return 'Welcome to the Rock, Paper, Scissors game!'

# Define the route for the game
@app.route('/play', methods=['POST'])
def play():
    # Check if request.json is None
    if request.json is None:
        return jsonify({'error': 'No JSON object provided in the request'}), 400

    # Check if 'choice' key is in request.json
    if 'choice' not in request.json:
        return jsonify({'error': 'No choice provided in the JSON object'}), 400

    
    # Get the user's choice from the request
    user_choice = request.json['choice']

    # Define the choices
    choices = ['rock', 'paper', 'scissors']

    # Get the computer's choice
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        result = 'You win!'
    elif user_choice == 'paper' and computer_choice == 'rock':
        result = 'You win!'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        result = 'You win!'
    else:
        result = 'Computer wins!'

    # Return the result
    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

# To run the application, execute the following command in the terminal:
# python app.py

# The application will start running on http://
# You can now make a POST request to http://localhost:5000/play with the following JSON payload:
# {
#     "choice": "rock"
# }
# The response will contain the user's choice, the computer's choice, and the result of the game.

# You can test the game by making multiple requests with different choices and observing the results.

