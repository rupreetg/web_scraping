#####################################################################################################################
#                                                                                                                   #
# User should be able to enter a prompt and system will search for corresponding URL                                #
# GPT will search correct URL, open a browser and take a screenshot out of it.                                      #
# Based on the screenshot, we'll use vision APIs to understand the screenshot, extract content out of it and        #
# give the result back to user by extracting text out of it.                                                        #
#                                                                                                                   #
# We'll use puppeteer in node.js to open URL and take screenshot.                                                   #    
# We'll use GPT4 to get the URLs                                                                                    #
# We'll use GPT4-vision API to understand the images.                                                               #
#                                                                                                                   #
# We'll have user give option to use GPT or Gemini                                                                  #
#                                                                                                                   #
# Inspiration: https://www.youtube.com/watch?v=VeQR17k7fiU - Easy Web Scraping                                      #                                                                             #
#####################################################################################################################     


import openailib
import utilities
from dotenv import load_dotenv
load_dotenv()


question = "Whats the age of Sam Altman?"

#Pass in the question to gpt and get the url for the answer
url = openailib.call_openai_chat(question)

#run puppeteer to take a screenshot of the url and save it as screenshot.jpg
utilities.run_node_subprocess("puppeteer.js", url)

# Function to encode the image
base64_image = utilities.encode_image("screenshot.jpg")

#call vision api to read from the image and get the answer to the quesiton
image_response = openailib.call_openai_vision(question, base64_image)

print(image_response)