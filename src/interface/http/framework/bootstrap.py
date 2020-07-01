from src.interface.http.framework.app import app
from src.interface.http.framework.exception_handlers import load_error_handlers
from src.interface.http.framework.routes_aggregator import aggregate_routes

load_error_handlers()
aggregate_routes(app)


def bootstrap_app():
    return app
