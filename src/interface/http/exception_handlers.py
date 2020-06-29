from fastapi import Request
from fastapi.responses import JSONResponse

from src.domain.vos.abstractions.value_object import ValueObject
from src.interface.http.bootstrap_http import app


@app.exception_handler(ValueObject.InvalidValue)
async def vo_invalid_value_handler(request: Request, exc: ValueObject.InvalidValue):
    return JSONResponse(
        status_code=422,
        content={
            'detail': [
                {
                    'loc': [
                        ''
                    ],
                    'msg': f'{exc.__class__.__name__}: \'{exc.value}\'',
                    'type': 'type_error.invalid_data_format'
                }
            ]
        }
    )
