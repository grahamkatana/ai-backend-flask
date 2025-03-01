from marshmallow import Schema, fields

from src.models.Agent import Agent


class AgentSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    image = fields.String(required=True)
    online = fields.Boolean(allow_none=True)
    attributes = fields.String(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        model = Agent
        load_instance = True
