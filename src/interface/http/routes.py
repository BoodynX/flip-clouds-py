from src.interface.http.bootstrap_http import router

import src.interface.http.flip_card_manager.routes

ROOT = '/'


@router.get(ROOT)
async def root():
    return {'message': 'Hello World'}
