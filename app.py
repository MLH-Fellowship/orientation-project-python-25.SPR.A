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
        return jsonify()

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

# Handles deletion of experience
@app.route('/resume/experience/<int:exp_id>', methods=['DELETE'])
def delete_experience(exp_id):
    try:
        if exp_id < 0 or exp_id >= len(data["experience"]):
            return jsonify({"message": "Resource doesn't exist"}), 404
        else:
            deleted_exp = data['experience'].pop(exp_id)
            # return jsonify({"message": "Experience Successfully Deleted", "deleted_experience": deleted_exp}), 200
            return jsonify({"message": "Experience Successfully Deleted"}), 200
    except Exception as e:
        print(f"Error :{e} ")
        return jsonify({"error": "An error occured"}), 500
    

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

# Handles the deletion of an existing education
@app.route('/resume/education/<int:edu_id>', methods=['DELETE'])
def delete_education(edu_id):
    try:
        if edu_id < 0 or edu_id >= len(data["education"]):
            return jsonify({"message": "Resource doesn't exist"}), 404
        else:
            del data['education'][edu_id]
            return jsonify({"message": "Education Successfully Deleted"}), 200
    except Exception as e:
        print(f"Error :{e} ")
        return jsonify({"error": "An error occured"}), 500


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

# Handles the deletion of Skills
@app.route('/resume/skill/<int:skill_id>', methods=['DELETE'])
def delete_skill(skill_id):
    try:
        if skill_id < 0 or skill_id >= len(data["skill"]):
            return jsonify({"message": "Resource doesn't exist"}), 404
        else:
            # skill_to_delete = data['skill'][skill_id];
            #data["skill"].remove(skill_to_delete);

            del data['skill'][skill_id]
            return jsonify({"message": "Skill Successfully Deleted"}), 200
    except Exception as e:
        print(f"Error: {e} ")
        return jsonify({"error": "An error occurred"}), 500
