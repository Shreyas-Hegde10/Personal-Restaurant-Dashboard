# Imports 
import os 
from dotenv import load_dotenv 
import requests  

# Loading environment variables from .env file 
load_dotenv('project.env') 

# Acessing environment variables via os module 
places_api_key = os.getenv("PLACES_API_KEY")  


