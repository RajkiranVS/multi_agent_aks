from fastapi import FastAPI, HTTPException, Query
from logic import get_summary

app = FastAPI()

@app.get("/summarize")
async def summarize(topic: str = Query(..., min_length=1, description="Topic to summarize")):
    try:
        summary = await get_summary(topic)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))