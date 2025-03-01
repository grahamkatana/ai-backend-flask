from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from src.config.extensions import db, migrate
from src.config.mail import mail
from src.config.bcrypt import bcrypt
from src.config.jwt import jwt
from routes import agents_router


app = Flask(__name__, static_url_path="/static")
CORS(app)
load_dotenv()

# load app config
app.config.from_object("src.config.config")
# initialize the database
db.init_app(app)
migrate.init_app(app, db, directory="db/migrations")
bcrypt.init_app(app)
jwt.init_app(app)
mail.init_app(app)

app.register_blueprint(agents_router.main, url_prefix="/api/v1/agents")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
