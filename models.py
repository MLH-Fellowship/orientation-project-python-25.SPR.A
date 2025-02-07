# pylint: disable=R0913

'''
Models for the Resume API. Each class is related to
'''

from dataclasses import dataclass
import json


@dataclass
class Experience:
    '''
    Experience Class
    '''
    title: str
    company: str
    start_date: str
    end_date: str
    description: str
    logo: str

    def model_dump_json(self):
        '''
        Dumps the class into a JSON string
        '''
        return json.dumps(self, default=lambda o: o.__dict__)

@dataclass
class Education:
    '''
    Education Class
    '''
    course: str
    school: str
    start_date: str
    end_date: str
    grade: str
    logo: str
    description: str

    def model_dump_json(self):
        '''
        Dumps the class into a JSON string
        '''
        return json.dumps(self, default=lambda o: o.__dict__)


@dataclass
class Skill:
    '''
    Skill Class
    '''
    name: str
    proficiency: str
    logo: str
