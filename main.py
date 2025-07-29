# main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world(): # Corrected function name to hello_world to avoid typo based on common Flask patterns
    print("Route '/' was accessed")  # Log to confirm it's hitting
    return render_template('index.html')

if __name__ == '__main__':
    # Flask runs on http://127.0.0.1:5000 by default
    # debug=True automatically reloads the server on code changes and provides a debugger
    app.run(debug=True)

# python main.py
# https://conversational-agents.cloud.google.com/projects/my-chatbot-463709/locations/global/agents/0dce91a3-d2d0-400d-a29e-b0100bd46a6b/(tools//right-panel:simulator)