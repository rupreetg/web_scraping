import google.generativeai as genai
import os
import constants
import json
import PIL.Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def call_google_chat(question):
    model = genai.GenerativeModel(constants.GOOGLE_MODEL)
    response = model.generate_content("""You are a web crawler and your job is to give URL back to the user for the asked question. 
                    Your response should be in the following format {\"url\": \"<url here>\"}. User question is: """ + question)
    jsonData = json.loads(response.candidates[0].content.parts[0].text)
    return jsonData["url"]

def call_google_vision(question, image_name):
    model = genai.GenerativeModel(constants.GOOGLE_VISION_MODEL)
    img = PIL.Image.open(image_name)
    response = model.generate_content([question, img])
    return response.candidates[0].content.parts[0].text
    