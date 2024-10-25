from pydantic import BaseModel, Field
from typing import Optional

class History(BaseModel):
    id: str = Field(..., description="The unique identifier for the history")
    incident_report: str = Field(..., description="The description of the incident report")
    process_note: Optional[str] = Field(None, description="A description of the process note")
    validation_result: str = Field(..., description="The result of the autism validation")

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "incident_report": "Sample Incident Report",
                "process_note": "This is a sample process note.",
                "validation_result": "This guy has strong autism",
            }
        }
