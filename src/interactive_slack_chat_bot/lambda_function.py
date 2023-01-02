import os
import json
import boto3
import ast
from urllib import parse

import slack_functions as slack

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

dynamodb = boto3.resource('dynamodb', region_name = 'ap-northeast-1')
conversations = dynamodb.Table('conversation')


def lambda_handler(event, context):
  channel = "C04G56FP3S7"
  receive_body = parse.parse_qs(event['body'])
  receive_payload = json.loads(receive_body["payload"][0])
  if (receive_payload['type'] == "shortcut" and receive_payload['callback_id'] == "shortcut_0000"):
    message = conversations.get_item( Key={'message_id':'m1'} )['Item']['message']
    value = json.dumps(json.loads(message)["blocks"])
    res = slack.post_channel_by_params(channel, {"blocks": value})
  elif (receive_payload['type'] == "block_actions" and receive_payload['actions'][0]["value"] == "block_actions_001"):
    message = conversations.get_item( Key={'message_id':'m2'} )['Item']['message']
    value = json.loads(message)
    res = slack.post_channel_by_params(channel, value)
  elif (receive_payload['type'] == "block_actions" and receive_payload['actions'][0]["value"] == "block_actions_002"):
    message = conversations.get_item( Key={'message_id':'m3'} )['Item']['message']
    value = json.loads(message)
    res = slack.post_channel_by_params(channel, value)
  elif (receive_payload['type'] == "block_actions" and receive_payload['actions'][0]["value"] == "block_actions_003"):
    res = slack.post_channel_by_params(channel, {"text": "未実装"})
  else:
    res = slack.post_channel_by_params(channel, {"text": "Out of Scope"})
    
  return (res)
