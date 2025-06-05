from fastapi import FastAPI, HTTPException, Query
from logic import get_planner_response

app = FastAPI()

@app.get("/plan")
async def plan(topic: str = Query(..., min_length=1, description="Topic to create a research plan for")):
    try:
        plan_text = await get_planner_response(topic)
        return {"plan": plan_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
