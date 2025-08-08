from fastapi import FastAPI
from .routers import health, connect_aws, scan, suggestions, github, artifacts

app = FastAPI(title="Agentic LLM-Ops")

app.include_router(health.router)
app.include_router(connect_aws.router)
app.include_router(scan.router)
app.include_router(suggestions.router)
app.include_router(github.router)
app.include_router(artifacts.router)
