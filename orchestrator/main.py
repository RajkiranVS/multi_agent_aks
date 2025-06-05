from fastapi import FastAPI
import uvicorn
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer

app = FastAPI()
exporter = AzureExporter(connection_string="InstrumentationKey=<YOUR_INSTRUMENTATION_KEY>")
tracer = Tracer(exporter=exporter, sampler=ProbabilitySampler(1.0))

@app.post("/run_pipeline")
def run_pipeline(task: str):
    with tracer.span(name="run_pipeline"):
        return {"status": "Pipeline executed", "task": task}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
