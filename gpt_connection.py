

from openai import OpenAI
import os
from dotenv import load_dotenv
from models import Experience, Education
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_improvement(model : Experience | Education):
    prompt = f"Improve the following description for the {model.__class__.__name__}: {model.description}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that improves descriptions for resumes."},
            {"role": "assistant", "content": "Here is the improved description:"},
            {"role": "system", "content": f"Consider the following information about the {model.__class__.__name__}: {model.model_dump_json()}"},
            {"role": "user", "content": prompt},
        ]
    )
    try:
        return response.choices[0].message.content
    except:
        return None



