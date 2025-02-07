'''
Tests in Pytest
'''
from app import app


def test_client():
    '''
    Makes a request and checks the message received is the same
    '''
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"


def test_experience():
    '''
    Add a new experience and then get all experiences. 
    
    Check that it returns the new experience in that list
    '''
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/experience',
                                     json=example_experience).json['id']
    response = app.test_client().get('/resume/experience')
    assert response.json[item_id] == example_experience



# def test_delete_experience():

#     example_experience = {
#         "title": "Mechanic",
#         "company": "Decepticons .Ent",
#         "start_date": "January 2020",
#         "end_date": "Present",
#         "description": "Hail Megatron",
#         "logo" : "example-log.png"
#     }
#     response = app.test_client().post('/resume/experience', json= example_experience)
#     assert response.status_code == 200
    
#     get_all_experiences = app.test_client().get('/resume/experience')
#     experience_id = len(get_all_experiences.json) - 1

#     delete_response = app.test_client().delete(f'/resume/experience/{experience_id}')
#     assert delete_response.status_code == 200
#     deleted_experience = delete_response.json['deleted_experience']

#     assert example_experience == deleted_experience

#     get_exp = app.test_client().get('/resume/experience')
#     for experience in get_exp.json:
#         assert experience != deleted_experience


def test_education():
    '''
    Add a new education and then get all educations. 
    
    Check that it returns the new education in that list
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }
    item_id = app.test_client().post('/resume/education',
                                     json=example_education).json['id']

    response = app.test_client().get('/resume/education')
    assert response.json[item_id] == example_education


def test_skill():
    '''
    Add a new skill and then get all skills. 
    
    Check that it returns the new skill in that list
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/skill',
                                     json=example_skill).json['id']

    response = app.test_client().get('/resume/skill')
    assert response.json[item_id] == example_skill

    response = app.test_client().get(f'/resume/skill/{item_id}')
    assert response.json == example_skill
