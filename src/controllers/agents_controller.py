from flask import jsonify
from src.models.Agent import Agent
from src.schemas.AgentSchema import AgentSchema


def get_all():
    try:
        agents = Agent.query.all()
        schema = AgentSchema(many=True)
        return jsonify({"data": schema.dump(agents)}), 200
    except Exception as e:
        print(e)
