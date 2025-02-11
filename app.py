'''
Flask Application
'''

from flask import Flask, jsonify, request

from models import Education, Experience, Skill

app = Flask(__name__)

data = {
    "experience": [
        Experience(
            "Software Developer",
            "A Cool Company",
            "October 2022",
            "Present",
            "Writing Python Code",
            "example-logo.png",
        )
    ],
    "education": [
        Education(
            "Computer Science",
            "University of Tech",
            "September 2019",
            "July 2022",
            "80%",
            "example-logo.png",
        )
    ],
    "skill": [Skill("Python", "1-2 Years", "example-logo.png")],
}


@app.route("/test")
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route("/resume/education", methods=["GET", "POST"])
def education():
    '''
    Handles education requests
    '''
    if request.method == "GET":
        return jsonify({})

    if request.method == "POST":
        return jsonify({})

    return jsonify({})


@app.route("/resume/skill", methods=["GET", "POST"])
@app.route('/resume/skill/<int:skill_id>', methods=['DELETE'])
def skill(skill_id = None):
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify([skill.__dict__ for skill in data["skill"]]), 200

    if request.method == 'POST':
        json_data = request.json
        try:
            # extract the data from the request
            name = json_data["name"]
            proficiency = json_data["proficiency"]
            logo = json_data["logo"]

            new_skill = Skill(name, proficiency, logo)

            data["skill"].append(new_skill)

            # return ID of new skill
            return jsonify(
                {"id": len(data["skill"]) - 1}
            ), 201

        except KeyError:
            return jsonify({"error": "Invalid request"}), 400

        except TypeError as e:
            return jsonify({"error": str(e)}), 400
    if request.method == "DELETE":
        try:
            if skill_id is None or skill_id < 0 or skill_id >= len(data["skill"]):
                return jsonify({"message": "Resource doesn't exist"}), 404
            else:   
                del data['skill'][skill_id]
                return jsonify({"message": "Skill Successfully Deleted"}), 200

        except Exception as e:      
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify({})
      
@app.route('/resume/skill/<int:skill_id>', methods=['GET'])
def get_skill(skill_id):
    '''
    Get a specific skill
    '''

    if request.method == "GET":
        try:
            return jsonify(data["skill"][skill_id].__dict__)
        except IndexError:
            return jsonify({"error": "Skill not found"}), 404
