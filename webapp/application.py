from fastapi import FastAPI

from . import endpoints
from .containers import Container


def create_app():
    container = Container()
    container.config.from_yaml("config.yml")
    container.wire(modules=[endpoints])

    fastapi_app = FastAPI()
    fastapi_app.container = container
    fastapi_app.include_router(endpoints.router)

    return fastapi_app


app = create_app()
