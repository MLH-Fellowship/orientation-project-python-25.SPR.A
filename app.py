'''
Flask Application
'''

from flask import Flask, jsonify, request
from models import Experience, Education, Skill
from gpt_connection import get_improvement
from validation import validate_experience, validate_education, validate_skill
from spell_check import spell_check

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
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png",
                  "I was head of the debate team at university")
    ],
    "skill": [Skill("Python", "1-2 Years", "example-logo.png")],
}


@app.route("/test")
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})

@app.route('/resume/spell_check', methods=['POST'])
def spell_check():
    json_data = request.json
    if json_data.get('description') and isinstance(json_data.get('description'), str):
        json_data['description'] = spell_check(json_data['description'])
    return jsonify({
        "before": request.json,
        "after": json_data
    })
  
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
            validated_data = validate_skill(json_data)

            data["skill"].append(validated_data)

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
        except (ValueError, TypeError, KeyError) as e:
            return jsonify({"error": f"Invalid request: {str(e)}"}), 400
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
