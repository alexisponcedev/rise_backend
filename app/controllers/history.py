from app.database.dynamodb import dynamodb
from botocore.exceptions import ClientError
from app.models.history import History

def generate_validation_result(incident_report: str, process_note: str) -> str:
    return "Generated validation result based on the given incident report and process note."

def create_history_item(history: History):
    
    validation_result = generate_validation_result(
        incident_report=history['incident_report'],
        process_note=history.get('process_note')
    )
    history['validation_result'] = validation_result
    
    """Create a history item in DynamoDB."""

    table = dynamodb.Table('ValidationHistory')
    try:
        response = table.put_item(Item=history.dict())
        return response
    except ClientError as e:
        raise RuntimeError(f"Failed to create history item: {e.response['Error']['Message']}")

def get_history_item(history_id: str):
    """Retrieve a history item from DynamoDB by ID."""
    table = dynamodb.Table('ValidationHistory')
    try:
        response = table.get_item(Key={'id': history_id})
        return response.get('Item')
    except ClientError as e:
        raise RuntimeError(f"Failed to retrieve history item: {e.response['Error']['Message']}")
