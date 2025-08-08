# Agentic LLM-Ops

Monorepo containing frontend (Next.js) and backend (FastAPI + Celery) for an Agentic LLM-Ops platform.

## Local Development

1. Copy `.env.example` to `.env` and adjust values.
2. Run `docker compose up --build`.
3. Visit http://localhost:3000 for the frontend.

## Structure
- `apps/frontend` – Next.js frontend.
- `apps/backend` – FastAPI API and Celery workers.
- `packages/prompts` – Prompt templates for the agent pipeline.
- `infra/local` – Docker compose for development.

## Tests
Run backend unit tests:

```bash
cd apps/backend
pytest
```
