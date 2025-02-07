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

    if request.method == 'POST':
        json_data = request.json
        try:
            validated_data = validate_experience(json_data)
            
            data["experience"].append(validated_data)
            return jsonify({"id": len(data["experience"]) - 1}), 201

        except (ValueError, TypeError, KeyError) as e:
            return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": f"Internal error: {str(e)}"}), 500


    return jsonify({"error": "Method not allowed"}), 405


@app.route('/resume/spell_check', methods=['POST'])
def spell_check():
    json_data = request.json
    if json_data.get('description') and isinstance(json_data.get('description'), str):
        json_data['description'] = spell_check(json_data['description'])
    return jsonify({
        "before": request.json,
        "after": json_data
    })
  
@app.route("/resume/education", methods=["GET", "POST"])
def education():
    '''
    Handles education requests
    '''
    
    if request.method == 'GET':
        return jsonify(data['education']), 200

    if request.method == 'POST':
        json_data = request.json
        try:
            validated_data = validate_education(json_data)
            data["education"].append(validated_data)
            
            return jsonify({"id": len(data["education"]) - 1}), 201
        except (ValueError, TypeError, KeyError) as e:
            return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": f"Internal error: {str(e)}"}), 500
        
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
def skill():
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

        except (ValueError, TypeError, KeyError) as e:
            return jsonify({"error": f"Invalid request: {str(e)}"}), 400

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
