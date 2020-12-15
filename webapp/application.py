from fastapi import FastAPI
from .containers import Container
from . import endpoints


app = FastAPI()


def create_app():
    container = Container()
    container.config.from_yaml("config.yml")
    container.wire(modules=[endpoints])

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)

    return app


app = create_app()
