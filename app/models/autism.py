from pydantic import BaseModel, Field
from typing import Optional

class AutismData(BaseModel):
    id: str = Field(..., description="The unique identifier for the autism data entry")
    user_id: str = Field(..., description="The unique identifier for the user associated with this autism data")
    communication_methods_aac: Optional[str] = Field(None, description="AAC communication methods used by the user")
    communication_methods_frequency: Optional[str] = Field(None, description="Frequency of communication methods")
    social_interactions_engagement: Optional[str] = Field(None, description="User's engagement in social interactions")
    social_interactions_response: Optional[str] = Field(None, description="User's response in social interactions")
    progress_monitoring_tools: Optional[str] = Field(None, description="Tools used for progress monitoring")
    progress_monitoring_data_methods: Optional[str] = Field(None, description="Methods for collecting progress monitoring data")
    behavioral_patterns_triggers: Optional[str] = Field(None, description="Triggers for behavioral patterns")
    behavioral_patterns_frequency: Optional[str] = Field(None, description="Frequency of behavioral patterns")
    sensory_processing_preferences: Optional[str] = Field(None, description="Preferences for sensory processing")
    sensory_processing_diet: Optional[str] = Field(None, description="Dietary preferences related to sensory processing")
    interests_strengths_activities: Optional[str] = Field(None, description="Activities related to interests and strengths")
    interests_strengths_skill_areas: Optional[str] = Field(None, description="Skill areas related to interests and strengths")
    health_wellbeing_sleep: Optional[str] = Field(None, description="Health and well-being related to sleep")
    health_wellbeing_dietary: Optional[str] = Field(None, description="Health and well-being related to dietary habits")
    routine_structure_schedule: Optional[str] = Field(None, description="Schedule related to routine structure")
    routine_structure_transition: Optional[str] = Field(None, description="Transitions related to routine structure")
    educational_support_goals: Optional[str] = Field(None, description="Goals for educational support")
    educational_support_methods: Optional[str] = Field(None, description="Methods for educational support")

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "user_id": "1",
                "communication_methods_aac": "Picture Exchange",
                "communication_methods_frequency": "Daily",
                "social_interactions_engagement": "Moderate",
                "social_interactions_response": "Positive",
                "progress_monitoring_tools": "Behavioral Charts",
                "progress_monitoring_data_methods": "Weekly Reports",
                "behavioral_patterns_triggers": "Loud Noises",
                "behavioral_patterns_frequency": "Daily",
                "sensory_processing_preferences": "Quiet Environments",
                "sensory_processing_diet": "Gluten-Free",
                "interests_strengths_activities": "Art and Music",
                "interests_strengths_skill_areas": "Creative Skills",
                "health_wellbeing_sleep": "8 hours",
                "health_wellbeing_dietary": "Balanced Diet",
                "routine_structure_schedule": "Fixed Daily Routine",
                "routine_structure_transition": "Gradual Transitions",
                "educational_support_goals": "Improve Communication Skills",
                "educational_support_methods": "One-on-One Support"
            }
        }
