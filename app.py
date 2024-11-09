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

# Helper function to validate input data
def validate_data(data, required_fields):
    return all(field in data for field in required_fields)


# Experience Routes
@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify([exp.__dict__ for exp in data.get("experience", [])])

    elif request.method == 'POST':
        new_data = request.get_json()
        required_fields = ["title", "company", "start_date", "end_date", "description", "logo"]
        
        if validate_data(new_data, required_fields):
            new_experience = Experience(**new_data)
            data["experience"].append(new_experience)
            return jsonify({"message": "Experience added"}), 201
        else:
            return jsonify({"error": "Invalid data format"}), 400


@app.route('/resume/experience/<int:exp_id>', methods=['GET', 'PUT', 'DELETE'])
def specific_experience(exp_id):
    '''
    Handle specific experience requests
    '''
    if exp_id >= len(data["experience"]) or exp_id < 0:
        return jsonify({"error": "Experience not found"}), 404

    experience = data["experience"][exp_id]

    if request.method == 'GET':
        return jsonify(experience.__dict__)

    elif request.method == 'PUT':
        updated_data = request.get_json()
        for key, value in updated_data.items():
            if hasattr(experience, key):
                setattr(experience, key, value)
        return jsonify({"message": "Experience updated"})

    elif request.method == 'DELETE':
        data["experience"].pop(exp_id)
        return jsonify({"message": "Experience deleted"}), 204


# Education Routes
@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify([edu.__dict__ for edu in data.get("education", [])])

    elif request.method == 'POST':
        new_data = request.get_json()
        required_fields = ["course", "school", "start_date", "end_date", "grade", "logo"]
        
        if validate_data(new_data, required_fields):
            new_education = Education(**new_data)
            data["education"].append(new_education)
            return jsonify({"message": "Education added"}), 201
        else:
            return jsonify({"error": "Invalid data format"}), 400


@app.route('/resume/education/<int:edu_id>', methods=['GET', 'PUT', 'DELETE'])
def specific_education(edu_id):
    '''
    Handle specific education requests
    '''
    if edu_id >= len(data["education"]) or edu_id < 0:
        return jsonify({"error": "Education not found"}), 404

    education = data["education"][edu_id]

    if request.method == 'GET':
        return jsonify(education.__dict__)

    elif request.method == 'PUT':
        updated_data = request.get_json()
        for key, value in updated_data.items():
            if hasattr(education, key):
                setattr(education, key, value)
        return jsonify({"message": "Education updated"})

    elif request.method == 'DELETE':
        data["education"].pop(edu_id)
        return jsonify({"message": "Education deleted"}), 204


# Skill Routes
@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles skill requests
    '''
    if request.method == 'GET':
        return jsonify([skill.__dict__ for skill in data.get("skill", [])])

    elif request.method == 'POST':
        new_data = request.get_json()
        required_fields = ["name", "proficiency", "logo"]
        
        if validate_data(new_data, required_fields):
            new_skill = Skill(**new_data)
            data["skill"].append(new_skill)
            return jsonify({"message": "Skill added"}), 201
        else:
            return jsonify({"error": "Invalid data format"}), 400


@app.route('/resume/skill/<int:skill_id>', methods=['GET', 'PUT', 'DELETE'])
def specific_skill(skill_id):
    '''
    Handle specific skill requests
    '''
    if skill_id >= len(data["skill"]) or skill_id < 0:
        return jsonify({"error": "Skill not found"}), 404

    skill = data["skill"][skill_id]

    if request.method == 'GET':
        return jsonify(skill.__dict__)

    elif request.method == 'PUT':
        updated_data = request.get_json()
        for key, value in updated_data.items():
            if hasattr(skill, key):
                setattr(skill, key, value)
        return jsonify({"message": "Skill updated"})

    elif request.method == 'DELETE':
        data["skill"].pop(skill_id)
        return jsonify({"message": "Skill deleted"}), 204


# Reordering Functionality
@app.route('/resume/reorder', methods=['POST'])
def reorder():
    '''
    Reorders Experience, Education, and Skill lists
    '''
    reorder_data = request.get_json()
    for category in ["experience", "education", "skill"]:
        if category in reorder_data:
            new_order = reorder_data[category]
            data[category] = [data[category][i] for i in new_order if i < len(data[category])]
    return jsonify({"message": "Reordering completed"}), 200


if __name__ == '__main__':
    app.run(debug=True)
