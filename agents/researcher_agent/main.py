from fastapi import FastAPI, HTTPException, Query
from .logic import get_researcher_response

app = FastAPI()

@app.get("/research")
async def do_research(topic: str = Query(..., min_length=1, description="Topic to research on")):
    try:
        research_text = await get_researcher_response(topic)
        return {"research": research_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))