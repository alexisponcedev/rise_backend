from app.database.dynamodb import dynamodb
from botocore.exceptions import ClientError
from app.models.history import History

def create_history_item(history: History):
    """Create a history item in DynamoDB."""
    table = dynamodb.Table('ValidationHistory')
    try:
        # Convert History model to dictionary for DynamoDB
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
