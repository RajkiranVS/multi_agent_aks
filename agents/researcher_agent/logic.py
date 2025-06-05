import os
import openai
import asyncio
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")

DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")

async def get_researcher_response(topic: str) -> str:
    # Azure OpenAI SDK currently is sync, so use run_in_executor for async FastAPI compatibility
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
        engine=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a research assistant, a highly knowledgable and methodical AI designed to assist users in conducting research, gathering information, and presenting well-organized, accurate, and relevant findings. Your goal is to help users efficiently navigate complex topics, ensuring they receive comprehensive and reliable information."},
            {"role": "user", "content": f"Plan a research process for: {topic}"}
        ],
        temperature=0.7,
        max_tokens=800
    ))
    return response["choices"][0]["message"]["content"]