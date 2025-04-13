from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_smorest import Api

def create_app(config_class='app.config.Config'):
    load_dotenv()

    app = Flask(__name__, static_folder='../../frontend/out')
    CORS(app)
    app.config.from_object(config_class)

    app.config["API_TITLE"] = "Invoice API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"  # Swagger docs available at root
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    from routes.root import blp as RootRoute
    from routes.invoice import blp as InvoiceRoute
    api.register_blueprint(RootRoute)
    api.register_blueprint(InvoiceRoute)

    return app