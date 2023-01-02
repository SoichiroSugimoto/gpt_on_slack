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
  guide_message = conversations.get_item(
            Key={'message_id':'m1'}
        )['Item']['message']
  receive_body = parse.parse_qs(event['body'])
  receive_payload = json.loads(receive_body["payload"][0])
  value = json.dumps(json.loads(guide_message)["blocks"])
  res = slack.post_channel_by_params(channel, {"blocks": value})
  return (res)
