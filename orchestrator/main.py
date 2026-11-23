import os
from fastapi import FastAPI
import uvicorn
from microsoft.opentelemetry import use_microsoft_opentelemetry
from pydantic import BaseModel


class PipelineRequest(BaseModel):
    task: str


applications_insights_enabled = os.getenv(
    "APPLICATIONINSIGHTS_CONNECTION_STRING")

if applications_insights_enabled:
    # Initialize the Microsoft OpenTelemetry Distro with Azure Monitor export.
    use_microsoft_opentelemetry(
        enable_azure_monitor=True,
        azure_monitor_enable_live_metrics=False,  # To disable live metrics
    )

app = FastAPI()


@app.get("/health")
def get_health_status():
    return {"status": "Healthy and running"}


@app.post("/run_pipeline")
def run_pipeline(req: PipelineRequest):
    return {"status": "Pipeline executed", "task": req.task}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
