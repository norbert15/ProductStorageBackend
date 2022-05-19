from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from api.routes.api import router


def get_application() -> FastAPI:

    application = FastAPI()

    origins = [
    "http://localhost",
    "http://localhost:4200",
    ]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router)

    return application


app = get_application()