"""This script creates a basic boto3 dynamodb resource target table
of foo with a simple get_user method"""
import boto3
from botocore.exceptions import ClientError

Table = boto3.resource("dynamodb").Table("foo")


def get_user(user_id):
    """This method uses a supplied user id to get an item
    from a dynamodb table"""
    try:
        ddb_response = Table.get_item(Key={"id": user_id})
        return ddb_response.get("Item")
    except ClientError as e:
        raise
