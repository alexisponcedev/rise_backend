from fastapi import FastAPI
from app.database.dynamodb import initialize_db
from app.routes.history import router as validation_router
from app.routes.user import router as user_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    initialize_db()

# Include routers separately
app.include_router(validation_router)
app.include_router(user_router)