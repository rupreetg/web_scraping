import constants
from openai import OpenAI
import os
import json

client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY') 

def call_openai_chat(question):
    response = client.chat.completions.create(
        model=constants.GPT_MODEL,
        messages=
        [
            {
                "role" : "system", 
                "content": """You are a web crawler and your job is to give URL back to the user for the asked question. 
                    Your response should be in the following format {\"url\": \"<url here>\"} """
            },
            {
                "role" : "user", 
                "content" : question
            }
        ],
        seed=345353543
    )

    jsonData = json.loads(response.choices[0].message.content)
    return jsonData["url"]

def call_openai_vision(question, base64_image):
    image_response = client.chat.completions.create(
    model=constants.GPT_VISION_MODEL,
    messages = 
    [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", "text": question
                },
                {
                    "type": "image", "image_url": 
                                    {
                                        "url": f"data:image/jpeg;base64,{base64_image}"
                                    }
                }
            ]
        }
    ],
    max_tokens=500
    )

    return image_response.choices[0].message.content