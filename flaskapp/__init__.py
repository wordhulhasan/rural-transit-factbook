"""Initialize Flask flaskapp."""
from flask import Flask


def init_app():
    """Construct core Flask application with embedded Dash flaskapp."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our core Flask flaskapp
        from . import routes

        # Import Dash application
        # from .plotlydash.dashboard import init_dashboard
        from .app1.app import init_dashboard
        from .app1.callbacks import init_callbacks

        app = init_dashboard(app)

        init_callbacks(app)

        return app.server
