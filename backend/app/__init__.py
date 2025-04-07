from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

def create_app(config_class='app.config.Config'):
    load_dotenv()

    app = Flask(__name__, static_folder='../../frontend/out')
    CORS(app)
    app.config.from_object(config_class)

    from routes.root import root
    app.register_blueprint(root)

    return app