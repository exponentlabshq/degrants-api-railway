# Stacks Proposal API

A minimal, testable, and deployable Flask API for managing Stacks grant proposals.

## ✅ Project Status: IMPLEMENTED & READY

**Features:**
- RESTful API for proposal submission and retrieval
- In-memory storage (easily extensible to database)
- Comprehensive test coverage
- Railway-ready deployment configuration

## 🏗️ Project Structure

```
degrants-api-railway/
├── app/
│   ├── __init__.py         # Package initialization
│   └── api.py              # Main Flask application
├── tests/
│   ├── __init__.py         # Test package
│   └── test_api.py         # Unit tests
├── requirements.txt         # Python dependencies
├── Procfile                # Railway deployment
├── run.py                  # Local development entrypoint
└── readme.md               # This file
```

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check - confirms API is running |
| GET | `/proposals` | Retrieve all submitted proposals |
| POST | `/proposals` | Submit a new proposal |
| GET | `/proposals/<id>` | Get a specific proposal by ID |

## 📝 Proposal Schema

```json
{
  "name": "string",
  "email_address": "string", 
  "timestamp": "string",
  "one_liner": "string",
  "project_description": "string",
  "impact": "string",
  "project_timelines_milestones_deliverables": "string",
  "overall_cost": "string",
  "budgeting": "string",
  "self_sustainability_plans": "string",
  "open_source": "string",
  "why_me": "string"
}
```

## 🧪 Testing

Run the test suite:
```bash
python3 -m pytest tests/ -v
```

**Test Coverage:**
- ✅ Health check endpoint
- ✅ Proposal creation and retrieval
- ✅ Error handling for invalid proposal IDs

## 🏃‍♂️ Local Development

1. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Run the API locally:
   ```bash
   python3 run.py
   ```
   
   **Note:** Runs on port 8000 to avoid macOS AirPlay conflicts

3. Test endpoints:
   ```bash
   curl http://localhost:8000/
   curl http://localhost:8000/proposals
   ```

## 🚂 Railway Deployment

1. **Initialize Git & Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Stacks Proposal API"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/degrants-api-railway.git
   git push -u origin main
   ```

2. **Deploy on Railway:**
   - Go to [Railway](https://railway.app)
   - Create new project → Deploy from GitHub repo
   - Railway automatically detects `Procfile` and runs `gunicorn run:app`

## 🔧 Technical Details

- **Framework:** Flask 3.0.3
- **WSGI Server:** Gunicorn 21.2.0
- **Testing:** Pytest 8.2.2
- **Architecture:** Factory pattern with `create_app()`
- **Storage:** In-memory list (stateless, perfect for Railway)

## 🎯 Design Principles

- **Minimal:** No bloat, easy to deploy
- **Testable:** Unit tests for all endpoints
- **Deployable:** Works out-of-the-box on Railway
- **Extensible:** Easy to swap in database later without touching tests

## 🔮 Future Enhancements

- Database integration (PostgreSQL/Redis)
- Authentication & authorization
- Rate limiting
- Proposal validation
- File uploads for project documents

---

**Ready for production deployment! 🚀**