import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError
from app.logger import setup_logger

load_dotenv()

logger = setup_logger(__name__)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def create_table():
    """Create the DynamoDB table if it does not exist."""
    try:
        table = dynamodb.create_table(
            TableName='ValidationHistory',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'  # String
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName='ValidationHistory')
        logger.info("Table created successfully.")
    except dynamodb.meta.client.exceptions.ResourceInUseException:
        logger.warning("Table already exists.")
    except ClientError as e:
        logger.error(f"Error creating table: {e.response['Error']['Message']}")
        raise  # Re-raise the exception after logging

def initialize_db():
    """Initialize the database by creating necessary tables."""
    logger.info("Initializing database...")
    create_table()