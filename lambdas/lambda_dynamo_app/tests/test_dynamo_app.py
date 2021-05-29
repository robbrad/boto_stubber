"""This test script runs tests agains the dynamoDB app"""
import pytest
from botocore.stub import ANY, Stubber

from ..src import dynamo_app

@pytest.fixture(scope="function",name="ddb_stub")
def ddb_stubber():
    """This stubs out the dynamodb call"""
    ddb_stub = Stubber(dynamo_app.Table.meta.client)
    ddb_stub.activate()
    yield ddb_stub
    ddb_stub.deactivate()

def test_user_exists(ddb_stub):
    """This test is the get_user method when the user exists in the table"""

    user_id = 'user123'
    get_item_params = {'TableName': ANY,
                       'Key': {'id': user_id}}
    get_item_response = {'Item': {'id': {'S': user_id},
                                  'name': {'S': 'Spam'}}}
    ddb_stub.add_response('get_item', get_item_response, get_item_params)

    result = dynamo_app.get_user(user_id)
    assert result.get('id') == user_id
    ddb_stub.assert_no_pending_responses()

def test_user_missing(ddb_stub):
    """This test is the get_user method when the user does not
    exist in the table"""

    user_id = 'user123'
    get_item_params = {'TableName': ANY,
                       'Key': {'id': user_id}}
    get_item_response = {}
    ddb_stub.add_response('get_item', get_item_response, get_item_params)

    result = dynamo_app.get_user(user_id)
    assert result is None
    ddb_stub.assert_no_pending_responses()
