from fastapi import FastAPI
from adapters.inbound.user import user_router

app = FastAPI()

app.include_router(user_router)
