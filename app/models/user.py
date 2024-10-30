from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    id: str = Field(..., description="The unique identifier for the user")
    first_name: str = Field(..., description="The user's first name")
    last_name: str = Field(..., description="The user's last name")
    gender: Optional[str] = Field(None, description="The user's gender")
    created_at: str = Field(..., description="The timestamp when the user was created")
    dob: str = Field(..., description="The date of birth of the user")
    indigenous_origin: Optional[str] = Field(None, description="The user's indigenous origin")
    country_of_birth: Optional[str] = Field(None, description="The country where the user was born")
    living_arrangement: Optional[str] = Field(None, description="The user's living arrangement")
    communication_method: Optional[str] = Field(None, description="The method of communication used by the user")
    residential_setting: Optional[str] = Field(None, description="The residential setting of the user")
    primary_disability_type: Optional[str] = Field(None, description="The primary type of disability")
    other_disability_type: Optional[str] = Field(None, description="Other types of disabilities, if any")
    autism_module: Optional[str] = Field(None, description="The autism module applicable to the user")
    tech_module: Optional[str] = Field(None, description="The technology module applicable to the user")
    care_model: Optional[str] = Field(None, description="The care model applicable to the user")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1",
                "first_name": "John",
                "last_name": "Doe",
                "gender": "male",
                "created_at": "2023-10-30T12:00:00Z",
                "dob": "2000-01-01",
                "indigenous_origin": "None",
                "country_of_birth": "USA",
                "living_arrangement": "Independent",
                "communication_method": "Verbal",
                "residential_setting": "Urban",
                "primary_disability_type": "Autism",
                "other_disability_type": "None",
                "autism_module": "behavior_module",
                "tech_module": "personal_care",
                "care_model": "NDIS"
            }
        }
