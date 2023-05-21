from fastapi import FastAPI
from routers import grid

app = FastAPI()

app.include_router(grid.router)
