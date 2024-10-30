from fastapi import APIRouter, HTTPException, status
from app.models.user import User
from app.controllers.user import create_user, get_user, update_user, delete_user
from typing import Any

router = APIRouter()

@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user_data(user: User) -> dict[str, Any]:
    """API endpoint to create a user."""
    try:
        user_data = user.dict(exclude_unset=True)
        response = create_user(User(**user_data))
        return {"message": "User created successfully", "response": response}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user_data(user_id: str):
    """API endpoint to retrieve a user by ID."""
    try:
        user = get_user(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with ID {user_id} not found"
            )
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_user_data(user_id: str, user: User):
    """API endpoint to update a user by ID."""
    try:
        user_data = user.dict(exclude_unset=True)
        updated_user = update_user(user_id, user_data)
        return {"message": "User updated successfully", "response": updated_user}
    except HTTPException as e:
        raise e 
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_data(user_id: str):
    """API endpoint to delete a user by ID."""
    try:
        delete_user(user_id)
        return {"message": "User deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
