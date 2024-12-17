from fastapi import FastAPI

import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

app = FastAPI()

@app.post("/")
async def query(q: str):
    
    load_dotenv(find_dotenv())

    apiKey = os.getenv("API_KEY")

    genai.configure(api_key=apiKey)
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(q)
    responseText = response.text.rstrip('\n')
    # print("\n\n",response.text,"\n")
    
    return {"message": responseText}





# @app.get("/")
# async def root():
    
#     load_dotenv(find_dotenv())

#     apiKey = os.getenv("API_KEY")

#     genai.configure(api_key=apiKey)
#     model = genai.GenerativeModel("gemini-1.5-flash")

#     response = model.generate_content("Explain how AI works in one sentence")
#     # print("\n\n",response.text,"\n")
    
#     return {"message": response.text}