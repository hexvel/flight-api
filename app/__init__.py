from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routes import router


def create_app():
    app = FastAPI()
    Base.metadata.create_all(bind=engine)
    app.include_router(router)
    return app


app = create_app()
