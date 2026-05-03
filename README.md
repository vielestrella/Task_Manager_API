# 📋 Postgres Task Manager

> A lightweight, production-ready REST API for managing tasks — built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, fully containerized with Docker.

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | [FastAPI](https://fastapi.tiangolo.com/) 0.115 |
| ORM | [SQLAlchemy](https://www.sqlalchemy.org/) 2.0 |
| Database | [PostgreSQL](https://www.postgresql.org/) 15 |
| Validation | [Pydantic](https://docs.pydantic.dev/) v2 |
| Server | [Uvicorn](https://www.uvicorn.org/) |
| Containerization | Docker + Docker Compose |
| Migrations | [Alembic](https://alembic.sqlalchemy.org/) |

---

## 📁 Project Structure

```
.
├── main.py            # FastAPI app & route definitions
├── models.py          # SQLAlchemy ORM models
├── schemas.py         # Pydantic request/response schemas
├── database.py        # DB engine, session & base setup
├── requirements.txt   # Python dependencies
├── Dockerfile         # App container definition
└── docker-compose.yml # Multi-container orchestration
```

---

## ⚡ Quick Start

### Prerequisites

- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) installed

### Run with Docker Compose

```bash
# Clone the repository
git clone https://github.com/vielestrella/Task_Manager_API
cd Task_Manager_API

# Start all services (app + database)
docker compose up --build
```

The API will be available at **http://localhost:8000**

Interactive API docs (Swagger UI): **http://localhost:8000/docs**

---

## 🔌 API Endpoints

### Base URL: `http://localhost:8000`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tasks` | Get all tasks |
| `POST` | `/tasks` | Create a new task |
| `PATCH` | `/tasks/{task_id}` | Toggle task completion status |
| `DELETE` | `/tasks/{task_id}` | Delete a task and return its data |

---

### 📥 Request & Response Schemas

#### Create a Task — `POST /tasks`

**Request body:**
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "is_completed": false
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "is_completed": false
}
```

#### Toggle Task Status — `PATCH /tasks/{task_id}`

No request body needed. Toggles `is_completed` between `true` and `false`.

**Response:**
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "is_completed": true
}
```

#### Delete a Task — `DELETE /tasks/{task_id}`

Returns the deleted task's data before removal.

---

## 🗄️ Data Model

```
Task
├── id            Integer   PK, auto-increment
├── title         String    indexed
├── description   String    nullable
└── is_completed  Boolean   default: false
```

---

## ⚙️ Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `postgresql://user:password@db:5432/task_db` | PostgreSQL connection string |

You can override these in `docker-compose.yml` or via a `.env` file.

---

## 🐳 Docker Details

- **App** runs on port `8000` (host) → `80` (container)
- **Database** runs on port `5432`
- The app depends on the `db` service and connects automatically

```yaml
# docker-compose.yml excerpt
app:
  build: .
  ports:
    - "8000:80"
  depends_on:
    - db
```

---

## 🔧 Local Development (without Docker)

```bash
# Create a virtual environment
python -m venv venv
source venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set the database URL
export DATABASE_URL=postgresql://user:password@localhost:5432/task_db

# Run the app
fastapi run main.py --port 80
```

---

## 📦 Dependencies

```
alembic==1.16.1
fastapi[standard]==0.115.12
psycopg2-binary==2.9.10
pydantic==2.11.4
SQLAlchemy==2.0.40
uvicorn==0.34.2
```

---
