import json
from app.api import create_app

def test_home():
    app = create_app()
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Stacks Proposal API running"

def test_add_and_get_proposal():
    app = create_app()
    client = app.test_client()

    proposal = {
        "name": "Test Proposal",
        "email_address": "test@example.com",
        "timestamp": "2024-08-21T12:00:00Z",
        "one_liner": "This is a test",
        "project_description": "Testing description",
        "impact": "Testing impact",
        "project_timelines_milestones_deliverables": "Phase 1",
        "overall_cost": "100",
        "budgeting": "Budget details",
        "self_sustainability_plans": "Plan details",
        "open_source": "yes",
        "why_me": "Because testing matters"
    }

    res = client.post("/proposals", data=json.dumps(proposal), content_type="application/json")
    assert res.status_code == 201
    data = res.get_json()
    assert data["proposal"]["name"] == "Test Proposal"

    res = client.get("/proposals/0")
    assert res.status_code == 200
    assert res.get_json()["email_address"] == "test@example.com"
