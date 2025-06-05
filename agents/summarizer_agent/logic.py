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

async def get_summary(topic: str) -> str:
    # Azure OpenAI SDK currently is sync, so use run_in_executor for async FastAPI compatibility
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
        engine=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a Summarizer agent, a highly efficient and precise AI designed to create clear, concise, and accuracte summaries of information provided by the user or retrieved from external sources. Your role is to distill complex information into easily digestible summaries, ensuring that key points are highlighted and unnecessary details are omitted. You excel at understanding context and delivering summaries that are both informative and to the point."},
            {"role": "user", "content": f"Plan a research process for: {topic}"}
        ],
        temperature=0.7,
        max_tokens=800
    ))
    return response["choices"][0]["message"]["content"]