

from openai import OpenAI
import os
from dotenv import load_dotenv
from models import Experience, Education
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def get_improvement(model : Experience | Education):
    prompt = f"Improve the following description for the {model.__class__.__name__}: {model.description}"
    return get_chatgpt_response(prompt)



