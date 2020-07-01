from src.interface.http.flip_card_manager.routes import *

ROOT = '/'


@router.get(ROOT)
async def root():
    return {'message': 'Hello World'}
