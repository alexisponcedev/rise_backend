from fastapi import FastAPI
from app.database.dynamodb import initialize_db
from app.routes.history import router as validation_router
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    initialize_db()

app.include_router(validation_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)