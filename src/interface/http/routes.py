from fastapi import APIRouter

router = APIRouter()

ROOT = '/'


@router.get(ROOT)
async def root():
    return {'message': 'Hello World'}
