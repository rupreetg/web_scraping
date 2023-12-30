User asks a question to the system and it ask LLM Model to give the most probable URL which contains the answer. 

Based on the URL, we use puppeteer to open the browser, take a snapshot of it and give this snapshot to LLM model using Vision API to get answer to the question. 

Both OpenAI's GPT 4 and Google Gemini for this POC.
