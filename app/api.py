from flask import Flask, request, jsonify

import json
import os

def create_app():
    app = Flask(__name__)

    # Load seed data on startup
    proposals = []
    seed_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'seed_proposals.json')
    
    try:
        with open(seed_file, 'r') as f:
            proposals = json.load(f)
    except FileNotFoundError:
        # If seed file doesn't exist, start with empty proposals
        proposals = []

    template = {
        "name": "",
        "bns_name": "",
        "email_address": "",
        "timestamp": "",
        "one_liner": "",
        "project_description": "",
        "impact": "",
        "project_timelines_milestones_deliverables": "",
        "overall_cost": "",
        "budgeting": "",
        "self_sustainability_plans": "",
        "open_source": "",
        "why_me": ""
    }

    @app.route("/")
    def home():
        return {"message": "Stacks Proposal API running"}

    @app.route("/proposals", methods=["GET"])
    def get_proposals():
        return jsonify(proposals)

    @app.route("/proposals", methods=["POST"])
    def add_proposal():
        data = request.json
        proposal = template.copy()
        for key in proposal.keys():
            if key in data:
                proposal[key] = data[key]
        proposals.append(proposal)
        return jsonify({"message": "Proposal added", "proposal": proposal}), 201

    @app.route("/proposals/<int:proposal_id>", methods=["GET"])
    def get_proposal(proposal_id):
        if proposal_id < 0 or proposal_id >= len(proposals):
            return jsonify({"error": "Proposal not found"}), 404
        return jsonify(proposals[proposal_id])

    return app
