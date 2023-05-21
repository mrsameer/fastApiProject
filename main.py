from fastapi import FastAPI
from routers import grid, iwm_data

app = FastAPI()

app.include_router(grid.router)
app.include_router(iwm_data.router)
