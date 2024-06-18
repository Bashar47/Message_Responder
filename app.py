from flask import Flask, render_template, request
import chat_api

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for handling the form submission
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    # Get response from ChatGPT
    response = chat_api.get_chatgpt_response(user_input, chat_api.phrases)
    return render_template('index.html', user_input=user_input, response=response)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
