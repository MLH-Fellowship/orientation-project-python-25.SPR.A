"""
Flask Application
"""

from flask import Flask, jsonify, request
from models import Experience, Education, Skill

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
    """
    Returns a JSON test message
    """
    return jsonify({"message": "Hello, World!"})


@app.route("/resume/experience", methods=["GET", "POST"])
def experience():
    """
    Handle experience requests
    """
    if request.method == "GET":
        return jsonify()

    if request.method == "POST":
        return jsonify({})

    return jsonify({})


@app.route("/resume/education", methods=["GET", "POST"])
def education():
    """
    Handles education requests
    """
    if request.method == "GET":
        return jsonify({})

    if request.method == "POST":
        return jsonify({})

    return jsonify({})


@app.route("/resume/skill", methods=["GET", "POST"])
def skill():
    """
    Handles Skill requests
    """
    if request.method == "GET":
        return jsonify([skill.__dict__ for skill in data["skill"]])

    if request.method == "POST":
        json_data = request.json
        try:
            # extract the data from the request
            name = json_data["name"]
            proficiency = json_data["proficiency"]
            logo = json_data["logo"]

            new_skill = Skill(name, proficiency, logo)

            data["skill"].append(new_skill)

            # return the new skill and its ID
            return jsonify(
                {"id": len(data["skill"]) - 1, "skill": new_skill.__dict__}
            ), 201
        
        except KeyError:
            return jsonify({"error": "Invalid request"}), 400
            
        except TypeError as e:
            return jsonify({"error": str(e)}), 400
