import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

apiKey = os.getenv("API_KEY")



