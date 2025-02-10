from models import Experience, Education, Skill

def validate_experience(json_data: dict):
    '''
    Validates the experience
    '''
    if 'spell_check' in json_data:
        del json_data['spell_check']
    try:
        return Experience(**json_data)
    except Exception as e:
        raise ValueError(f"Invalid experience format: {e}")

def validate_education(json_data: dict):
    '''
    Validates the education
    '''
    if 'spell_check' in json_data:
        del json_data['spell_check']
    try:
        return Education(**json_data)
    except Exception as e:
        raise ValueError(f"Invalid education format: {e}")

def validate_skill(json_data: dict):
    '''
    Validates the skill
    '''
    if 'spell_check' in json_data:
        del json_data['spell_check']
    try:
        return Skill(**json_data)
    except Exception as e:
        raise ValueError(f"Invalid skill format: {e}")


data = {
    "experience": {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png",
        "spell_check": True
    },
    "education": {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png",
        "description": "I was head of the debate team at university"
    },
    "skill": {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }
}

print(validate_experience(data['experience']))
print(validate_education(data['education']))
print(validate_skill(data['skill']))