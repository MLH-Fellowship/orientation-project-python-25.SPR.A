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


@app.route("/resume/experience", methods=["GET", "POST"])
@app.route("/resume/experience/<int:index>", methods=["GET"])
def experience(index=None):
    '''
    Handle experience requests
    GET: Returns all experiences or a specific experience by index
    POST: Creates a new experience
    '''
    if request.method == "GET":
        if index is not None:
            try:
                return jsonify(data["experience"][index])
            except IndexError:
                return jsonify({"error": "Experience not found"}), 404
        return jsonify(data["experience"]), 200

    if request.method == "POST":
        try:
            new_experience = request.get_json()
            if not new_experience:
                return jsonify({"error": "No data provided"}), 400
            # validate required fields
            required_fields = [
                "title",
                "company",
                "start_date",
                "end_date",
                "description",
                "logo",
            ]
            if not all(field in new_experience for field in required_fields):
                return jsonify({"error": "Missing required fields"}), 400

            experience_obj = Experience(**new_experience)
            data["experience"].append(experience_obj)
            return jsonify({"id": len(data["experience"]) - 1}), 201


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

        except TypeError as e:
            return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": f"Internal error: {str(e)}"}), 500


    return jsonify({"error": "Method not allowed"}), 405

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
def skill():
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

    return jsonify({})

@app.route('/resume/skill/<int:skill_id>', methods=['GET'])
def get_skill(skill_id):
    '''
    Get a specific skill
    '''
    try:
        return jsonify(data["skill"][skill_id].__dict__)
    except IndexError:
        return jsonify({"error": "Skill not found"}), 404
