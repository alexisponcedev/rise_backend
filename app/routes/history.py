from fastapi import APIRouter, HTTPException, status
from app.models.history import History
from app.controllers.history import create_history_item, get_history_item

router = APIRouter()

@router.post("/validation/", status_code=status.HTTP_201_CREATED)
async def create_history(history: History):
    """API endpoint to create a history item."""
    try:
        response = create_history_item(history)
        return {"message": "History item created successfully", "response": response}
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/validation/{history_id}", status_code=status.HTTP_200_OK)
async def read_item(history_id: str):
    """API endpoint to retrieve a history item by ID."""
    try:
        item = get_history_item(history_id)
        if item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"History item with ID {history_id} not found"
            )
        return item
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
