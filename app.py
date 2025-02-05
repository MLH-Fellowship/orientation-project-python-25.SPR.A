'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill
from gpt_connection import get_improvement
app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png",
                  "I was head of the debate team at university")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify()

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/reword_description', methods=['GET'])
def reword_description():
    '''
    Rewords the description using GPT
    '''
    model = None
    try:
        model = Experience(**request.json)
    except:
        model = Education(**request.json)

    if model is None:
        return jsonify({"error": "Invalid request"}), 400

    response = get_improvement(model)
    if response is None:
        return jsonify({"error": "Failed to get improvement"}), 500
    
    return jsonify({"response": response})

@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})
