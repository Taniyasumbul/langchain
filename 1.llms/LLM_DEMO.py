from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load token from .env
load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize client
client = InferenceClient(model="google/flan-t5-large", token=token)

# Run inference (NO 'task' param here)
response = client.text_generation(
    prompt="What is the capital of India?",
    max_new_tokens=50
)

print(response)

