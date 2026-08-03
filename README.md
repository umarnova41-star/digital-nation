# Digital Nation Platform (MVP) — Backend (FastAPI)

Short description
This repository contains the FastAPI backend stubs for the Digital Nation Platform MVP. It currently includes:
- FastAPI app bootstrap: `backend/app/main.py`
- Simple routers stubs: `backend/app/api/v1/routers/{auth.py, citizens.py}`
- Minimal in-memory demo-store for quick local testing.

Quickstart (development)
1. Extract the ZIP and open a terminal in the project root.

2. Create & activate a Python virtual environment
- Linux / macOS:
  python -m venv .venv
  source .venv/bin/activate
- Windows (PowerShell):
  python -m venv .venv
  .\\.venv\\Scripts\\Activate.ps1

3. Install minimal deps
  pip install --upgrade pip
  pip install -r requirements.txt

4. Run the FastAPI server (from the `backend` folder)
- From repo root:
  uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
- Or change directory:
  cd backend
  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

5. Test endpoints
- Health:
  curl http://localhost:8000/health
- Citizens:
  GET  http://localhost:8000/api/v1/citizens/
  POST http://localhost:8000/api/v1/citizens/  (JSON: {"national_id":"123","first_name":"Ali","last_name":"Hassan"})
- Auth (stub):
  GET http://localhost:8000/api/v1/auth/me  (add Authorization header for demo)

Notes
- This is a starter scaffold. Next steps: DB integration (Postgres + SQLAlchemy), Keycloak integration, docker-compose dev environment.
