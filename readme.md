# Stacks Proposal API

A minimal, testable, and deployable Flask API for managing Stacks grant proposals.

## ✅ Project Status: IMPLEMENTED & READY WITH SEED DATA

**Features:**
- RESTful API for proposal submission and retrieval
- **Pre-populated with 3 realistic Stacks proposals** (seed data)
- In-memory storage (easily extensible to database)
- Comprehensive test coverage
- Railway-ready deployment configuration

## 🏗️ Project Structure

```
degrants-api-railway/
├── app/
│   ├── __init__.py         # Package initialization
│   └── api.py              # Main Flask application
├── data/
│   └── seed_proposals.json # Pre-populated proposal data
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
| GET | `/proposals` | Retrieve all submitted proposals (includes seed data) |
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

## 🌱 Seed Data

The API comes pre-populated with 3 realistic Stacks ecosystem proposals:

1. **Zero Authority** - DeGrants DAO Onchain & Open Source UX Toolkit
2. **Stacks DeFi Labs** - Bitcoin-Backed Yield Farming Protocol
3. **Clarity Dev Tools** - Comprehensive Testing Framework for Clarity Smart Contracts

**Example: Zero Authority Proposal Structure**
```json
{
  "name": "Zero Authority",
  "email_address": "dao@zeroauthority.xyz",
  "timestamp": "2024-06-13T18:32:16Z",
  "one_liner": "DeGrants DAO Onchain & Open Source UX Toolkit",
  "project_description": "DeGrants DAO Onchain enhances decentralized autonomous organizations with streamlined on-chain governance solutions, fostering transparency and community-driven decision-making. The Open Source UX Toolkit aims to enhance user experience in decentralized ecosystems, offering accessible, customizable tools to enhance interaction and governance within blockchain communities.",
  "impact": "The DeGrants DAO Onchain and Open Source UX Toolkit aims to significantly impact the Stacks community by enhancing decentralized governance and user experience. It aims to increase participation in DAOs and improve voting efficiency. It fosters transparency and community trust through accessible tools. For the Open Source UX Toolkit, the impact includes better usability and customization options, promoting broader adoption and innovation in blockchain governance.",
  "project_timelines_milestones_deliverables": "DeGrants DAO Onchain: 6-8 weeks with smart contract development, voting mechanisms, and testnet deployment. Open Source UX Toolkit: 6-8 weeks with UX research, prototype development, and community adoption drive.",
  "overall_cost": "3200",
  "budgeting": "$1000 DeGrants DAO Onchain & $2200 Open Source UX Toolkit",
  "self_sustainability_plans": "Open source release and community adoption drive to ensure long-term sustainability and community contributions.",
  "open_source": "Yes; open source",
  "why_me": "With my tenure in the Stacks ecosystem since 2019, my dedicated involvement with hodlstx since 2021, and our ongoing commitment through the Zero Authority live podcast since the same year, I've gained deep-rooted experience and understanding of our community's needs and evolution."
}
```

**Benefits:**
- ✅ **Realistic starting state** for developers testing your API
- ✅ **Consistent data** across deployments
- ✅ **Version controlled** with your codebase
- ✅ **Easy to modify** without touching code

## 🧪 Testing

Run the test suite:
```bash
python3 -m pytest tests/ -v
```

**Test Coverage:**
- ✅ Health check endpoint
- ✅ Proposal creation and retrieval
- ✅ Error handling for invalid proposal IDs
- ✅ Seed data loading functionality

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
   curl http://localhost:8000/proposals  # Returns seed data + any new proposals
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

**Your API will start with 3 realistic proposals already loaded!**

## 🔧 Technical Details

- **Framework:** Flask 3.0.3
- **WSGI Server:** Gunicorn 21.2.0
- **Testing:** Pytest 8.2.2
- **Architecture:** Factory pattern with `create_app()`
- **Storage:** In-memory list with JSON seed data loading
- **Seed Data:** Loaded on startup from `data/seed_proposals.json`

## 🎯 Design Principles

- **Minimal:** No bloat, easy to deploy
- **Testable:** Unit tests for all endpoints
- **Deployable:** Works out-of-the-box on Railway
- **Extensible:** Easy to swap in database later without touching tests
- **Realistic:** Starts with meaningful data for immediate testing

## 🔮 Future Enhancements

- Database integration (PostgreSQL/Redis)
- Authentication & authorization
- Rate limiting
- Proposal validation
- File uploads for project documents
- Dynamic seed data management

## 📊 Current Implementation

- **Repository:** https://github.com/exponentlabshq/degrants-api-railway
- **Status:** Fully implemented with seed data
- **Tests:** All passing
- **Production:** https://web-production-09f1.up.railway.app
- **Ready for:** Production use

---

**Successfully deployed to production with realistic starter data! 🚀**