import os
import json
import boto3
import ast
from urllib import parse

import slack_functions as slack
import openai_functions as opai

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

dynamodb = boto3.resource('dynamodb', region_name = 'ap-northeast-1')
conversations = dynamodb.Table('conversation')

def usage_guide(receive_payload):
  channel = "C04G56FP3S7"
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

def lambda_handler(event, context):
  receive_body = []
  try:
    receive_body = parse.parse_qs(event['body'])
    receive_payload = json.loads(receive_body["payload"][0])
  except:
    receive_payload = json.loads(event['body'])
  if (receive_payload['type'] == 'url_verification'):
    return {
      'statusCode': 200,
      'body': json.dumps( {'challenge': receive_payload['challenge'] } )
    }
  elif (receive_payload["type"] == "shortcut" or receive_payload["type"] == "block_actions"):
    slack.post_channel_message("C04G56FP3S7", "this is shortcut")
    # response = usage_guide(event)
  elif (receive_payload["type"] == "event_callback" and
        receive_payload["event"]["user"] != "U04HAFAP9FW" and
        int(json.loads(event['headers']['X-Slack-Retry-Num'])) == 1):
    request_text = ''
    if ('thread_ts' in receive_payload["event"]):
      request_text = slack.get_text_element_as_thread(receive_payload['event']['channel'], receive_payload['event']['thread_ts'])
    else:
      request_text = slack.get_text_element(receive_payload)
    reply_text = opai.openai_prompt(request_text)
    response = slack.post_channel_reply("C04G56FP3S7", reply_text, receive_payload["event"]["ts"])
  else:
    response == None
  return (response)