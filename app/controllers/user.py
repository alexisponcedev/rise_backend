from app.database.dynamodb import dynamodb
from botocore.exceptions import ClientError
from app.models.user import User
from typing import Optional, Dict

TABLE_NAME="User"
table = dynamodb.Table('User')

def create_user(user: User) -> User:
    try:
        response = table.put_item(Item=user.dict())
        return response
    except ClientError as e:
        raise Exception(f"Error creating user: {e.response['Error']['Message']}")

def get_user(user_id: str) -> Optional[User]:
    try:
        response = table.get_item(
            Key={'id': user_id}
        )
        if 'Item' in response:
            item = response['Item']
            return User(**item)
        return None
    except ClientError as e:
        raise Exception(f"Error retrieving user: {e.response['Error']['Message']}")

def update_user(user_id: str, user_data: Dict) -> User:
    update_expression = "SET "
    expression_attribute_values = {}
    
    for key, value in user_data.items():
        update_expression += f"{key} = :{key}, "
        expression_attribute_values[f":{key}"] = value    
    
    update_expression = update_expression[:-2] 
    
    try:
        table.update_item(
            Key={'id': user_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        return get_user(user_id)
    except ClientError as e:
        raise Exception(f"Error updating user: {e.response['Error']['Message']}")

def delete_user(user_id: str) -> None:
    try:
        table.delete_item(
            Key={'id': user_id}
        )
    except ClientError as e:
        raise Exception(f"Error deleting user: {e.response['Error']['Message']}")