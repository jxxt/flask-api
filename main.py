from fastapi import FastAPI

import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

app = FastAPI()


@app.post("/")
async def q(query: str):

    load_dotenv(find_dotenv())

    apiKey = os.getenv("API_KEY")

    genai.configure(api_key=apiKey)
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(query)
    responseText = response.text.rstrip('\n')

    return {"message": responseText}
