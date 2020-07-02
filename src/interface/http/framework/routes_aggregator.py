from src.interface.http.contexts.flip_card_manager.routes import router as flip_card_manager_router
from src.interface.http.routes import router as root_router


def aggregate_routes(app):
    app.include_router(root_router)
    app.include_router(flip_card_manager_router)

    return app
