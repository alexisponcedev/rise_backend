from pydantic import BaseModel, Field
from typing import Optional
from user import User

class DietaryPlan(BaseModel):
    id: str = Field(..., description="The unique identifier for the dietary plan")
    user_id: User = Field(..., description="The user associated with this dietary plan")
    meal_type: str = Field(..., description="The type of meal (breakfast, lunch, dinner)")
    starter: Optional[str] = Field(None, description="The starter for the meal")
    main_course: Optional[str] = Field(None, description="The main course for the meal")
    dessert: Optional[str] = Field(None, description="The dessert for the meal")
    dislikes: Optional[str] = Field(None, description="Foods the user dislikes")
    likes: Optional[str] = Field(None, description="Foods the user likes")
    allergic_foods: Optional[str] = Field(None, description="Foods the user is allergic to")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1",
                "user_id": "1",
                "meal_type": "lunch",
                "starter": "Salad",
                "main_course": "Grilled Chicken",
                "dessert": "Ice Cream",
                "dislikes": "Broccoli",
                "likes": "Pasta",
                "allergic_foods": "Nuts"
            }
        }
