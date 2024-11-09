'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

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
                  "example-logo.png")
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
        return jsonify(data["experience"])
    
    if request.method == 'POST':
        experience_data = request.get_json()
        data["experience"].append(experience_data)
        return jsonify({
            "id": len(data["experience"]) - 1
        })
    
    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify(data["education"])
    
    if request.method == 'POST':
        education_data = request.get_json()
        data["education"].append(education_data)
        return jsonify({
            "id": len(data["education"]) - 1
        })
    
    return jsonify({})

@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify(data["skill"])
    
    if request.method == 'POST':
        skill_data = request.get_json()
        data["skill"].append(skill_data)
        return jsonify({
            "id": len(data["skill"]) - 1
        })
    
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)