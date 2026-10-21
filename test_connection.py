from dotenv import load_dotenv
from openai import OpenAI

# Load API credentials from .env
load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Reply with exactly: OpenAI connection successful"
)

print(response.output_text)